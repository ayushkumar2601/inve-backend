# InventoryPulse Dependency Analysis Report

## 1. Frontend Dependency Analysis (`/frontend`)

### Environment & Package Manager
- **Required Node.js Version**: `>= 18.0.0` (Recommended: `Node.js 20.x LTS`)
- **Package Manager**: `npm` (Lockfile: `package-lock.json`) or `bun` (Lockfile: `bun.lockb`). Both lockfiles are present.

### Required Core Production Dependencies
| Package | Version | Purpose |
| :--- | :--- | :--- |
| `react` & `react-dom` | `^18.3.1` | Core UI React framework |
| `react-router-dom` | `^6.26.2` | Client-side routing (`/`) |
| `@tanstack/react-query` | `^5.56.2` | Data fetching, caching, and state sync |
| `recharts` | `^2.12.7` | Dashboard charting and analytics visualization |
| `lucide-react` | `^0.462.0` | Modern SVG iconography |
| `react-hook-form` & `zod` | `^7.53.0` / `^3.23.8` | Form handling & schema validation |
| `@radix-ui/react-*` | Various (`^1.1.0` to `^2.2.1`) | Accessible headless UI primitives |
| `tailwindcss` & `clsx` | `^3.4.11` / `^2.1.1` | Utility-first CSS styling and class merging |
| `sonner` | `^1.5.0` | Toast notifications |

### Development Dependencies
| Package | Version | Purpose |
| :--- | :--- | :--- |
| `vite` | `^5.4.1` | Fast frontend bundler and dev server |
| `typescript` | `^5.5.3` | TypeScript compiler and static typing |
| `@vitejs/plugin-react-swc` | `^3.5.0` | Fast SWC-based React fast-refresh plugin |
| `eslint` | `^9.9.0` | Linter |

### Missing Packages / Dependency Status (Frontend)
- **Status**: **Complete**. All UI components referenced in `Dashboard.tsx`, `CustomerSupportChat.tsx`, and `ApiTestComponent.tsx` have matching package entries in `package.json`. No missing packages identified.

---

## 2. Backend Dependency Analysis (`/backend`)

### Environment & Package Manager
- **Required Python Version**: `>= 3.11.0` (Recommended: `3.11.x` or `3.12.x`)
- **Package Manager**: `pip` with `requirements.txt`
- **Virtual Environment Recommendation**:
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt
  ```

### Required Backend Dependencies (`requirements.txt`)
| Package | Specified Version | Purpose |
| :--- | :--- | :--- |
| `Flask` | `2.3.3` | Core web application framework |
| `flask-restx` | `1.1.0` | REST API OpenAPI 2.0 / Swagger documentation |
| `flask-cors` | `4.0.0` | CORS handling for cross-origin frontend requests |
| `Werkzeug` | `2.3.7` | WSGI web application library |
| `pymongo` | `4.5.0` | MongoDB Atlas driver |
| `snowflake-connector-python` | `3.3.1` | Snowflake Data Warehouse connector |
| `requests` | `2.31.0` | HTTP client for calling MiniMax LLM API |
| `numpy` / `pandas` / `scipy` / `scikit-learn` | `1.24.3` / `2.0.3` / `1.11.2` / `1.3.0` | Scientific computing & baseline ML forecasting |
| `temporalio` | `1.4.0` | Temporal Python SDK for workflow orchestration |
| `structlog` | `23.1.0` | Structured JSON application logging |
| `pydantic` | `2.3.0` | Data validation and type coercion |
| `python-dotenv` | `1.0.0` | `.env` configuration loader |
| `pytest` / `pytest-asyncio` | `7.4.2` / `0.21.1` | Unit and integration testing framework |
| `dataclasses-json` | `0.5.14` | JSON serialization for Python dataclasses |

### Transitive & Implicit Dependencies Audited
- `certifi`: Imported in `db_service.py` (`import certifi`) for SSL certificate verification against MongoDB Atlas. Automatically installed alongside `pymongo` and `requests`.

### Missing Packages / Dependency Status (Backend)
- **Status**: **Complete**. All modules imported across `app.py`, `config.py`, `routes/*`, `services/*`, and `models/*` are correctly declared in `requirements.txt`.
