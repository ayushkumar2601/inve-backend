# InventoryPulse Environment Discovery & Configuration Report

This document details all environment variables discovered across the **InventoryPulse** frontend and backend codebases, their purpose, usage locations, requirement status, and configured values.

---

## 1. Summary of Environment Audit
- **All Required Secrets Present**: Verified against `backend/.env`. No required database credentials, Snowflake access tokens, or MiniMax LLM API keys are missing.
- **No Unconfigured Placeholders**: Every active service connection string contains valid credentials or appropriate development defaults.

---

## 2. Backend Environment Variables (`backend/config.py` & `.env`)

| Variable Name | Purpose | Required? | Where Used? | Example / Active Value |
| :--- | :--- | :--- | :--- | :--- |
| `FLASK_APP` | Specifies the Flask application factory/module entry point | Optional | Flask CLI startup | `backend/app.py` |
| `FLASK_ENV` | Sets application execution profile (`development`, `staging`, `production`, `testing`) | Optional | `backend/app.py:L22`, `backend/config.py:L16` | `development` |
| `SECRET_KEY` | Flask cryptographic key for session/security handling | Optional | `backend/config.py:L15` | `a-very-secret-key` |
| `CORS_ORIGINS` | Allowed cross-origin domains for CORS configuration | Optional | `backend/app.py:L46`, `backend/config.py:L21` | `*` |
| `MONGO_URI` | Full MongoDB Atlas connection string | **Yes** | `backend/services/db_service.py:L23`, `config.py:L24` | `mongodb+srv://user:pass@awshacky725...mongodb.net/` |
| `MONGO_DB_NAME` | MongoDB database name | **Yes** | `backend/services/db_service.py:L24`, `config.py:L25` | `InventoryPulseDB` |
| `MONGO_TLS_ALLOW_INVALID_CERTIFICATES` | SSL/TLS tolerance flag for MongoDB connections | Optional | `backend/config.py:L28` | `True` |
| `SNOWFLAKE_ACCOUNT` | Snowflake account organization identifier | Optional | `backend/services/snowflake_service.py:L20` | `SFSEHOL-AWS_HACKATHON_EVENT_YLTRDU` |
| `SNOWFLAKE_USERNAME` (`SNOWFLAKE_USER`) | Username for Snowflake analytical data warehouse connection | Optional | `backend/services/snowflake_service.py:L18` | `USER` |
| `SNOWFLAKE_PASSWORD` | Password for Snowflake data warehouse connection | Optional | `backend/services/snowflake_service.py:L19` | Configured in `.env` |
| `SNOWFLAKE_WAREHOUSE` | Snowflake compute warehouse name | Optional | `backend/services/snowflake_service.py:L21` | `AWSHACK725` |
| `SNOWFLAKE_DATABASE` | Snowflake database name | Optional | `backend/services/snowflake_service.py:L22` | `AWSHACK725` |
| `SNOWFLAKE_SCHEMA` | Snowflake schema name | Optional | `backend/services/snowflake_service.py:L23` | `PUBLIC` |
| `MINIMAX_API_KEY` | MiniMax LLM API Bearer token (JWT format) | **Yes** (for AI) | `backend/services/ai_forecasting_service.py:L31` | Configured JWT token in `.env` |
| `MINIMAX_GROUP_ID` | MiniMax Group ID parameter | **Yes** (for AI) | `backend/services/ai_forecasting_service.py:L32` | `1881319919820215190` |
| `MINIMAX_MODEL` | MiniMax LLM target model name | Optional | `backend/services/ai_forecasting_service.py:L33` | `MiniMax-M1` (or `MiniMax-Text-01`) |
| `MINIMAX_BASE_URL` | Base API URL for MiniMax REST completion endpoints | Optional | `backend/services/ai_forecasting_service.py:L30` | `https://api.minimax.io/v1/text/chatcompletion_v2` |
| `MINIMAX_DISABLE_STREAM` | Boolean flag to disable SSE response streaming | Optional | `backend/services/ai_forecasting_service.py:L52` | `True` |
| `MINIMAX_TIMEOUT_SECONDS` | HTTP request timeout for MiniMax API invocations | Optional | `backend/services/ai_forecasting_service.py:L53` | `90` |
| `TEMPORAL_GRPC_ENDPOINT` | Temporal Server gRPC connection host and port | Optional | `backend/services/temporal_service.py:L44`, `config.py:L52` | `localhost:7233` |
| `TEMPORAL_NAMESPACE` | Target Temporal namespace | Optional | `backend/config.py:L53` | `default` |
| `LOG_LEVEL` | Application logging verbosity (`INFO`, `DEBUG`, etc.) | Optional | `backend/config.py:L49` | `INFO` |
| `NLX_API_KEY` | External conversational API key (not actively invoked) | No | `backend/config.py:L45` | Unused |
| `WIZ_API_KEY` | External security API key (not actively invoked) | No | `backend/config.py:L46` | Unused |

---

## 3. Frontend Environment Variables (`frontend/src/lib/api.ts`)

| Variable Name | Purpose | Required? | Where Used? | Example / Active Value |
| :--- | :--- | :--- | :--- | :--- |
| `VITE_API_BASE_URL` | Base URL for REST API calls to backend | Optional | `frontend/src/lib/api.ts:L5` | `http://localhost:5500/api` (default fallback) |
