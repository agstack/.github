#!/usr/bin/env python3
"""Regenerate profile/README.md from the live organisation.

    gh auth status              # needs read access to the org
    python3 scripts/update-profile.py [--check]

The prose, the domain grouping and the one-line descriptions are curated
here. Every number, date, language and star count is read from GitHub at
run time, so the page cannot drift from the org the way a hand-edited table
does (the previous version said 46 repositories for six months while the
org had 42).

Rules the script enforces so they do not have to be remembered:
- only PUBLIC repositories are listed; a private repo linked from a public
  page is a dead link for every visitor
- every public repository must be placed in a section, or the script fails
  and names it, so a new repo cannot be created and forgotten
- ``--check`` exits 1 if the committed README differs from what the live
  org would produce; wire it to a schedule and the page stays current

Requires the ``gh`` CLI, authenticated.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from collections import Counter
from datetime import datetime, timedelta, timezone
from pathlib import Path

ORG = "agstack"
README = Path(__file__).resolve().parents[1] / "profile" / "README.md"

# Repositories that belong to the org's plumbing rather than its catalogue.
SKIP = {".github"}

# Curated: section -> (intro, [(repo, description)]). Order is the page order.
# Descriptions are one line each and say what the thing is, in the repo's own
# words where it has them. Language, last push and stars are filled in live.
SECTIONS: list[tuple[str, str, list[tuple[str, str]]]] = [
    (
        "Asset Registry -- Geospatial Identity",
        "Deterministic, unique identifiers (GeoIDs) for any geospatial feature -- farm fields, "
        "GPS points, forests, countries. The foundation for traceability across agricultural "
        "supply chains.",
        [
            ("asset-registry", "AR 1.0 -- current production. Flask-based GeoID registration and resolution"),
            ("user-registry", "User accounts, JWT issuance, API keys for AR 1.0"),
            ("asset-registry-fe", "Frontend web application for the Asset Registry"),
            ("autogeobound", "Automatic field boundary detection from satellite imagery"),
            (
                "pancake",
                "AI-native geospatial datastore and DPI services: field-ownership grants as SD-JWT "
                "credentials with revocation and a signed audit ledger, scheduled vendor-data ingestion, "
                "content-addressed BITE store queryable by GeoID",
            ),
        ],
    ),
    (
        "INATrace -- Supply Chain Traceability",
        "Open-source blockchain-based track and trace for agricultural supply chains. Covers the "
        "full journey from farmer to consumer.",
        [
            ("inatrace", "Meta repo -- links backend, frontend, mobile, and blockchain components"),
            ("inatrace-backend", "Java/Spring backend for INATrace"),
            ("inatrace-frontend", "Angular frontend for INATrace"),
            ("inatrace-mobile", "Mobile app for farmer data collection"),
            ("inatrace-coffee-network", "Blockchain smart contracts for coffee supply chain"),
        ],
    ),
    (
        "TraceFoodChain",
        "Flutter-based app and web portal for tracing goods along food production chains.",
        [("tracefoodchain", "Flutter app/webapp for food chain traceability")],
    ),
    (
        "OpenAgri Platform",
        "A modular, microservices-based digital agriculture platform from the EU OpenAgri project -- "
        "farm calendars, irrigation, pest management, weather, reporting, and more.",
        [
            ("OpenAgri-Bootstrap-Deployment", "Modular configuration and deployment of all OpenAgri services"),
            ("OpenAgri-GateKeeper", "JWT-based authentication and access proxy"),
            ("OpenAgri-FarmCalendar", "Digital farm calendar -- operations, observations, parcels, assets"),
            ("OpenAgri-WeatherService", "Weather forecasts and critical agricultural indicators"),
            ("OpenAgri-IrrigationManagement", "Evapotranspiration calculations and soil moisture analysis"),
            ("OpenAgri-PestAndDiseaseManagement", "Pest and disease monitoring and management"),
            ("OpenAgri-ReportingService", "PDF report generation for agricultural data visualization"),
            ("OpenAgri-UserDashboard", "Web UI exposing all OpenAgri service functionality"),
            ("OpenAgri-OCSM", "OpenAgri Common Semantic Model"),
        ],
    ),
    (
        "AgriOS -- Farm Management ERP",
        "Farm management on Odoo 18: farmers and farmer groups, plots, trade, and training, as "
        "installable addons. AGPL-3, contributed by Advance Insight.",
        [
            (
                "AgriOS",
                "Odoo 18 addons -- `agrios_farmer`, `agrios_plot`, `agrios_trade`, `agrios_training`, "
                "theme and demo data (branch `18.0`)",
            ),
        ],
    ),
    (
        "TerraTrac -- EUDR Compliance",
        "Mobile field boundary capture and deforestation risk assessment for EU Deforestation "
        "Regulation compliance.",
        [
            (
                "TerraTrac-field-app",
                "Mobile app for recording plot geolocations (point and polygon), offline-capable, "
                "CSV/GeoJSON export",
            ),
            (
                "TerraTrac-validator-portal",
                "Upload plot data, run deforestation risk assessment via WHisp API, generate reports",
            ),
        ],
    ),
    (
        "AI and Knowledge Graphs",
        "LLM integration, knowledge graph frameworks, and AI-driven agriculture recommendations.",
        [
            ("palefire", "Pale Fire -- LLM + knowledge graph integration framework"),
            ("arias", "AI for agriculture"),
            ("ag-rec", "Open-source agriculture recommendations from Cooperative Extension Services"),
        ],
    ),
    (
        "Weather, Climate, and Pests",
        "Weather data infrastructure -- from data ingest and pre-processing to forecasting and "
        "serving -- and the weather-driven pest and disease models built on it.",
        [
            ("weather-server", "Weather data ingest, pre-processing, and serving pipeline"),
            ("weather-forecast", "Global weather forecast using NOAA NCEP/NOMADS data"),
            (
                "opensource-pestmodels",
                "Hierarchical pest and disease modelling framework -- 13 models, 19 crops, 54 threats; "
                "Python wheel, FastAPI and MCP server",
            ),
            ("pest-models", "Weather-driven pest models (earlier work)"),
            ("field-carbon-model", "Field-specific carbon model leveraging SMAP L4C"),
        ],
    ),
    (
        "Communication and Messaging",
        "",
        [
            ("MessageCast", "Messaging platform"),
            ("messagecast-backend", "MessageCast backend"),
            ("messagecast-frontend", "MessageCast frontend"),
        ],
    ),
    (
        "Governance, Community, and Infrastructure",
        "",
        [
            ("governance", "AgStack governance documents"),
            ("meetings", "Agendas and notes from AgStack project meetings"),
            ("LF-europe", "EU subproject for AgStack"),
            ("agstack-website", "Website code for agstack.org"),
            ("agstack-landscape", "l.agstack.org landscape"),
            ("artwork", "Logos and artwork"),
            ("jupyter-notebooks", "Demo notebooks showing API usage examples"),
        ],
    ),
]

LANG_SHORT = {"Jupyter Notebook": "Jupyter"}

LICENCE_NAMES = {
    "apache-2.0": ("Apache 2.0", "https://www.apache.org/licenses/LICENSE-2.0"),
    "eupl-1.2": ("EUPL 1.2", "https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12"),
    "mpl-2.0": ("MPL 2.0", "https://www.mozilla.org/en-US/MPL/2.0/"),
    "mit": ("MIT", "https://opensource.org/license/mit"),
    "agpl-3.0": ("AGPL 3.0", "https://www.gnu.org/licenses/agpl-3.0.html"),
    "gpl-3.0": ("GPL 3.0", "https://www.gnu.org/licenses/gpl-3.0.html"),
    "cc-by-4.0": ("CC BY 4.0", "https://creativecommons.org/licenses/by/4.0/"),
}


def live_repos() -> dict[str, dict]:
    out = subprocess.check_output(
        [
            "gh", "repo", "list", ORG, "--limit", "500", "--visibility", "public",
            "--json", "name,description,pushedAt,stargazerCount,forkCount,primaryLanguage,"
            "licenseInfo,isArchived,issues",
        ],
        text=True,
    )
    return {r["name"]: r for r in json.loads(out)}


def render(repos: dict[str, dict], today: datetime) -> str:
    listed = {name for _, _, rows in SECTIONS for name, _ in rows}
    public = {n for n in repos if n not in SKIP}
    unplaced = sorted(public - listed)
    if unplaced:
        sys.exit(f"public repositories not placed in any section: {unplaced}. Add them to SECTIONS.")
    missing = sorted(listed - public)
    if missing:
        sys.exit(f"listed but not public (or gone): {missing}. Remove them, or they are dead links.")

    catalogue = [repos[n] for n in sorted(public)]
    n_repos = len(repos)  # GitHub's own count includes .github
    stars = sum(r["stargazerCount"] for r in catalogue)
    forks = sum(r["forkCount"] for r in catalogue)
    cutoff = today - timedelta(days=183)
    active = sum(1 for r in catalogue if datetime.fromisoformat(r["pushedAt"].replace("Z", "+00:00")) > cutoff)
    langs = Counter(
        (r["primaryLanguage"] or {}).get("name") for r in catalogue if r["primaryLanguage"]
    )
    lang_list = ", ".join(name for name, _ in langs.most_common())
    licences = Counter((r["licenseInfo"] or {}).get("key") for r in catalogue)

    def row(name: str, desc: str) -> str:
        r = repos[name]
        lang = (r["primaryLanguage"] or {}).get("name") or "--"
        lang = LANG_SHORT.get(lang, lang)
        archived = " *(archived)*" if r["isArchived"] else ""
        return (
            f"| [**{name}**](https://github.com/{ORG}/{name}){archived} | {desc} | {lang} | "
            f"{r['pushedAt'][:10]} | {r['stargazerCount']} |"
        )

    parts: list[str] = []
    parts.append(f"""<div align="center">

<img src="https://agstack.org/wp-content/uploads/sites/35/2021/02/logo-color.svg" alt="AgStack Foundation" width="280"/>

# The AgStack Foundation

### Open Digital Infrastructure for Agriculture & Food

[![Website](https://img.shields.io/badge/Website-agstack.org-2ea44f?style=for-the-badge)](https://agstack.org)
[![Landscape](https://img.shields.io/badge/Landscape-l.agstack.org-blue?style=for-the-badge)](https://l.agstack.org)
[![License](https://img.shields.io/badge/License-Apache_2.0-orange?style=for-the-badge)](#license)
[![Repos](https://img.shields.io/badge/Repositories-{n_repos}-purple?style=for-the-badge)](#project-catalog)

*A Linux Foundation project -- the global open-source community building, maintaining, and evolving the digital infrastructure for agriculture and food.*

</div>

---

## Community at a Glance

| Metric | Value |
|--------|-------|
| **Repositories** | {n_repos} |
| **Combined Stars** | {stars} |
| **Combined Forks** | {forks} |
| **Active Repos** (pushed in last 6 months) | {active} |
| **Languages** | {lang_list} |

---

## Project Catalog

Every public repository in the AgStack organisation, organized by domain. Click any project name to visit the repo.
""")

    for title, intro, rows in SECTIONS:
        parts.append("---\n")
        parts.append(f"### {title}\n")
        if intro:
            parts.append(f"> {intro}\n")
        parts.append("| Repo | Description | Lang | Last Push | Stars |")
        parts.append("|------|-------------|------|-----------|-------|")
        parts.extend(row(name, desc) for name, desc in rows)
        parts.append("")

    top = [k for k, _ in licences.most_common() if k in LICENCE_NAMES]
    links = " or ".join(f"[{LICENCE_NAMES[k][0]}]({LICENCE_NAMES[k][1]})" for k in top[:2])
    others = ", ".join(LICENCE_NAMES[k][0] for k in top[2:])
    unlicensed = licences.get(None, 0)

    parts.append(f"""---

## Getting Started

**Explore a project:** Click any repo link above to see its README, issues, and code.

**Run OpenAgri locally:** Start with [OpenAgri-Bootstrap-Deployment](https://github.com/agstack/OpenAgri-Bootstrap-Deployment) for a one-command setup of all OpenAgri services.

**Register a field boundary:** Use the [asset-registry](https://github.com/agstack/asset-registry) API or the [TerraTrac mobile app](https://github.com/agstack/TerraTrac-field-app) to capture field boundaries and receive GeoIDs.

**Trace a supply chain:** Deploy [INATrace](https://github.com/agstack/inatrace) for blockchain-based farm-to-consumer traceability.

**Run a farm:** Install the [AgriOS](https://github.com/agstack/AgriOS) addons on Odoo 18 for farmer, plot, trade and training management.

**Model a pest:** [opensource-pestmodels](https://github.com/agstack/opensource-pestmodels) serves 13 weather-driven pest and disease models over FastAPI and MCP.

**Build with AI:** Use [Palefire](https://github.com/agstack/palefire) to integrate LLMs with agricultural knowledge graphs.

---

## Contributing

AgStack is open to contributors of all levels. Every repo has its own issues list and contribution guidelines. Good starting points:

- Browse repos tagged [`hacktoberfest`](https://github.com/search?q=org%3Aagstack+topic%3Ahacktoberfest&type=repositories) for beginner-friendly issues.
- Join the conversation in [meetings](https://github.com/agstack/meetings).
- Read the [governance](https://github.com/agstack/governance) docs for project structure and decision-making.

---

## License

Most AgStack projects are licensed under {links}; others use {others}. {unlicensed} repositories declare no license file yet. See each repository for its specific license.

---

<div align="center">

*AgStack is a [Linux Foundation](https://www.linuxfoundation.org/) project.*

<sub>Catalog generated from the live organisation on {today:%Y-%m-%d} by <code>scripts/update-profile.py</code>.</sub>

</div>
""")
    return "\n".join(parts)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true", help="exit 1 if profile/README.md is out of date")
    args = ap.parse_args()

    today = datetime.now(timezone.utc)
    text = render(live_repos(), today)
    if args.check:
        current = README.read_text() if README.exists() else ""
        # the date stamp alone should not fail the check
        strip = lambda s: "\n".join(ln for ln in s.splitlines() if "Catalog generated" not in ln)  # noqa: E731
        if strip(current) != strip(text):
            sys.exit("profile/README.md is out of date; run scripts/update-profile.py")
        print("profile/README.md is current")
        return
    README.write_text(text)
    print(f"wrote {README} ({len(text.encode())} bytes)")


if __name__ == "__main__":
    main()
