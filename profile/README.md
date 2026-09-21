<div align="center">

<img src="https://agstack.org/wp-content/uploads/sites/35/2021/02/logo-color.svg" alt="AgStack Foundation" width="280"/>

# The AgStack Foundation

### Open Digital Infrastructure for Agriculture & Food

[![Website](https://img.shields.io/badge/Website-agstack.org-2ea44f?style=for-the-badge)](https://agstack.org)
[![Landscape](https://img.shields.io/badge/Landscape-l.agstack.org-blue?style=for-the-badge)](https://l.agstack.org)
[![License](https://img.shields.io/badge/License-Apache_2.0-orange?style=for-the-badge)](#license)
[![Repos](https://img.shields.io/badge/Repositories-42-purple?style=for-the-badge)](#project-catalog)

*A Linux Foundation project -- the global open-source community building, maintaining, and evolving the digital infrastructure for agriculture and food.*

</div>

---

## Community at a Glance

| Metric | Value |
|--------|-------|
| **Repositories** | 42 |
| **Combined Stars** | 197 |
| **Combined Forks** | 93 |
| **Active Repos** (pushed in last 6 months) | 12 |
| **Languages** | Python, TypeScript, Jupyter Notebook, JavaScript, Kotlin, SCSS, Java, Dart, Julia |

---

## Project Catalog

Every public repository in the AgStack organisation, organized by domain. Click any project name to visit the repo.

---

### Asset Registry -- Geospatial Identity

> Deterministic, unique identifiers (GeoIDs) for any geospatial feature -- farm fields, GPS points, forests, countries. The foundation for traceability across agricultural supply chains.

| Repo | Description | Lang | Last Push | Stars |
|------|-------------|------|-----------|-------|
| [**asset-registry**](https://github.com/agstack/asset-registry) | AR 1.0 -- current production. Flask-based GeoID registration and resolution | Python | 2026-05-15 | 10 |
| [**user-registry**](https://github.com/agstack/user-registry) | User accounts, JWT issuance, API keys for AR 1.0 | Python | 2025-12-31 | 2 |
| [**asset-registry-fe**](https://github.com/agstack/asset-registry-fe) | Frontend web application for the Asset Registry | TypeScript | 2024-05-09 | 0 |
| [**autogeobound**](https://github.com/agstack/autogeobound) | Automatic field boundary detection from satellite imagery | Jupyter | 2025-02-20 | 7 |
| [**pancake**](https://github.com/agstack/pancake) | AI-native geospatial datastore and DPI services: field-ownership grants as SD-JWT credentials with revocation and a signed audit ledger, scheduled vendor-data ingestion, content-addressed BITE store queryable by GeoID | Jupyter | 2026-09-18 | 7 |

---

### INATrace -- Supply Chain Traceability

> Open-source blockchain-based track and trace for agricultural supply chains. Covers the full journey from farmer to consumer.

| Repo | Description | Lang | Last Push | Stars |
|------|-------------|------|-----------|-------|
| [**inatrace**](https://github.com/agstack/inatrace) | Meta repo -- links backend, frontend, mobile, and blockchain components | -- | 2026-02-23 | 1 |
| [**inatrace-backend**](https://github.com/agstack/inatrace-backend) | Java/Spring backend for INATrace | Java | 2026-09-18 | 11 |
| [**inatrace-frontend**](https://github.com/agstack/inatrace-frontend) | Angular frontend for INATrace | TypeScript | 2025-12-24 | 1 |
| [**inatrace-mobile**](https://github.com/agstack/inatrace-mobile) | Mobile app for farmer data collection | TypeScript | 2025-12-24 | 0 |
| [**inatrace-coffee-network**](https://github.com/agstack/inatrace-coffee-network) | Blockchain smart contracts for coffee supply chain | TypeScript | 2025-11-20 | 1 |

---

### TraceFoodChain

> Flutter-based app and web portal for tracing goods along food production chains.

| Repo | Description | Lang | Last Push | Stars |
|------|-------------|------|-----------|-------|
| [**tracefoodchain**](https://github.com/agstack/tracefoodchain) | Flutter app/webapp for food chain traceability | Dart | 2026-09-04 | 4 |

---

### OpenAgri Platform

> A modular, microservices-based digital agriculture platform from the EU OpenAgri project -- farm calendars, irrigation, pest management, weather, reporting, and more.

| Repo | Description | Lang | Last Push | Stars |
|------|-------------|------|-----------|-------|
| [**OpenAgri-Bootstrap-Deployment**](https://github.com/agstack/OpenAgri-Bootstrap-Deployment) | Modular configuration and deployment of all OpenAgri services | Python | 2026-06-09 | 7 |
| [**OpenAgri-GateKeeper**](https://github.com/agstack/OpenAgri-GateKeeper) | JWT-based authentication and access proxy | Python | 2026-04-22 | 8 |
| [**OpenAgri-FarmCalendar**](https://github.com/agstack/OpenAgri-FarmCalendar) | Digital farm calendar -- operations, observations, parcels, assets | Python | 2026-05-08 | 12 |
| [**OpenAgri-WeatherService**](https://github.com/agstack/OpenAgri-WeatherService) | Weather forecasts and critical agricultural indicators | Python | 2026-08-06 | 23 |
| [**OpenAgri-IrrigationManagement**](https://github.com/agstack/OpenAgri-IrrigationManagement) | Evapotranspiration calculations and soil moisture analysis | Python | 2026-04-23 | 10 |
| [**OpenAgri-PestAndDiseaseManagement**](https://github.com/agstack/OpenAgri-PestAndDiseaseManagement) | Pest and disease monitoring and management | Python | 2025-10-16 | 10 |
| [**OpenAgri-ReportingService**](https://github.com/agstack/OpenAgri-ReportingService) | PDF report generation for agricultural data visualization | Python | 2026-04-27 | 8 |
| [**OpenAgri-UserDashboard**](https://github.com/agstack/OpenAgri-UserDashboard) | Web UI exposing all OpenAgri service functionality | TypeScript | 2025-10-10 | 5 |
| [**OpenAgri-OCSM**](https://github.com/agstack/OpenAgri-OCSM) | OpenAgri Common Semantic Model | Jupyter | 2025-10-07 | 7 |

---

### AgriOS -- Farm Management ERP

> Farm management on Odoo 18: farmers and farmer groups, plots, trade, and training, as installable addons. AGPL-3, contributed by Advance Insight.

| Repo | Description | Lang | Last Push | Stars |
|------|-------------|------|-----------|-------|
| [**AgriOS**](https://github.com/agstack/AgriOS) | Odoo 18 addons -- `agrios_farmer`, `agrios_plot`, `agrios_trade`, `agrios_training`, theme and demo data (branch `18.0`) | Python | 2026-03-02 | 1 |

---

### TerraTrac -- EUDR Compliance

> Mobile field boundary capture and deforestation risk assessment for EU Deforestation Regulation compliance.

| Repo | Description | Lang | Last Push | Stars |
|------|-------------|------|-----------|-------|
| [**TerraTrac-field-app**](https://github.com/agstack/TerraTrac-field-app) | Mobile app for recording plot geolocations (point and polygon), offline-capable, CSV/GeoJSON export | Kotlin | 2025-10-24 | 1 |
| [**TerraTrac-validator-portal**](https://github.com/agstack/TerraTrac-validator-portal) | Upload plot data, run deforestation risk assessment via WHisp API, generate reports | SCSS | 2025-06-17 | 0 |

---

### AI and Knowledge Graphs

> LLM integration, knowledge graph frameworks, and AI-driven agriculture recommendations.

| Repo | Description | Lang | Last Push | Stars |
|------|-------------|------|-----------|-------|
| [**palefire**](https://github.com/agstack/palefire) | Pale Fire -- LLM + knowledge graph integration framework | Python | 2026-09-01 | 6 |
| [**arias**](https://github.com/agstack/arias) | AI for agriculture | -- | 2025-09-18 | 0 |
| [**ag-rec**](https://github.com/agstack/ag-rec) | Open-source agriculture recommendations from Cooperative Extension Services | JavaScript | 2022-01-08 | 12 |

---

### Weather, Climate, and Pests

> Weather data infrastructure -- from data ingest and pre-processing to forecasting and serving -- and the weather-driven pest and disease models built on it.

| Repo | Description | Lang | Last Push | Stars |
|------|-------------|------|-----------|-------|
| [**weather-server**](https://github.com/agstack/weather-server) | Weather data ingest, pre-processing, and serving pipeline | Julia | 2021-12-16 | 21 |
| [**weather-forecast**](https://github.com/agstack/weather-forecast) | Global weather forecast using NOAA NCEP/NOMADS data | Python | 2023-04-02 | 3 |
| [**opensource-pestmodels**](https://github.com/agstack/opensource-pestmodels) | Hierarchical pest and disease modelling framework -- 13 models, 19 crops, 54 threats; Python wheel, FastAPI and MCP server | Python | 2026-08-31 | 1 |
| [**pest-models**](https://github.com/agstack/pest-models) | Weather-driven pest models (earlier work) | Python | 2021-10-15 | 2 |
| [**field-carbon-model**](https://github.com/agstack/field-carbon-model) | Field-specific carbon model leveraging SMAP L4C | Python | 2024-03-13 | 4 |

---

### Communication and Messaging

| Repo | Description | Lang | Last Push | Stars |
|------|-------------|------|-----------|-------|
| [**MessageCast**](https://github.com/agstack/MessageCast) | Messaging platform | JavaScript | 2023-02-09 | 4 |
| [**messagecast-backend**](https://github.com/agstack/messagecast-backend) | MessageCast backend | -- | 2023-06-14 | 0 |
| [**messagecast-frontend**](https://github.com/agstack/messagecast-frontend) | MessageCast frontend | -- | 2023-06-14 | 0 |

---

### Governance, Community, and Infrastructure

| Repo | Description | Lang | Last Push | Stars |
|------|-------------|------|-----------|-------|
| [**governance**](https://github.com/agstack/governance) | AgStack governance documents | -- | 2024-10-30 | 2 |
| [**meetings**](https://github.com/agstack/meetings) | Agendas and notes from AgStack project meetings | -- | 2024-08-19 | 0 |
| [**LF-europe**](https://github.com/agstack/LF-europe) | EU subproject for AgStack | -- | 2025-07-16 | 0 |
| [**agstack-website**](https://github.com/agstack/agstack-website) | Website code for agstack.org | JavaScript | 2024-09-09 | 0 |
| [**agstack-landscape**](https://github.com/agstack/agstack-landscape) | l.agstack.org landscape | -- | 2021-02-26 | 2 |
| [**artwork**](https://github.com/agstack/artwork) | Logos and artwork | -- | 2021-04-19 | 0 |
| [**jupyter-notebooks**](https://github.com/agstack/jupyter-notebooks) | Demo notebooks showing API usage examples | Jupyter | 2023-09-02 | 4 |

---

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

Most AgStack projects are licensed under [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) or [EUPL 1.2](https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12); others use MIT, MPL 2.0, CC BY 4.0, GPL 3.0. 10 repositories declare no license file yet. See each repository for its specific license.

---

<div align="center">

*AgStack is a [Linux Foundation](https://www.linuxfoundation.org/) project.*

<sub>Catalog generated from the live organisation on 2026-09-21 by <code>scripts/update-profile.py</code>.</sub>

</div>
