# InventoryPulse Complete API Documentation (Generated from Code)

Base URL: `http://localhost:5500/api`
Prefixes registered in `backend/app.py`:
- `/auth`: Authentication endpoints
- `/products`: Inventory product CRUD & filtering
- `/suppliers`: Supplier management & performance
- `/orders`: Purchase orders management
- `/users`: User and RBAC profile endpoints
- `/alerts`: System alerts and notification workflows
- `/system`: System health check and database diagnostics
- `/ai`: Advanced AI forecasting & predictive insights

---

## 1. Authentication Namespace (`/auth`)

### POST `/api/auth/login`
- **Method**: `POST`
- **Input Schema**: `{"username": "string", "password": "string"}`
- **Output Schema**: `{"message": "string", "status": "string", "user": "string", "note": "string"}`
- **Status Codes**: `200 OK`
- **Description**: User login endpoint (Authentication simplified for hackathon demo).

### GET `/api/auth/status`
- **Method**: `GET`
- **Input Schema**: None
- **Output Schema**: `{"message": "string", "status": "string", "user": "string", "note": "string"}`
- **Status Codes**: `200 OK`
- **Description**: Get current authentication state.

---

## 2. System Health Namespace (`/system`)

### GET `/api/system/health`
- **Method**: `GET`
- **Input Schema**: None
- **Output Schema**:
  ```json
  {
    "status": "ok | degraded",
    "timestamp": "ISO-8601",
    "version": "1.0.0",
    "environment": "development",
    "dependencies": {
      "mongodb": "connected | error",
      "temporal": "configured | not_configured",
      "minimax": "configured | not_configured",
      "snowflake": "connected | error"
    }
  }
  ```
- **Status Codes**: `200 OK` (All healthy), `503 Service Unavailable` (Degraded dependency)
- **Description**: Full diagnostic health check auditing MongoDB Atlas, Snowflake, Temporal, and MiniMax LLM configurations.

### GET `/api/system/stats`
- **Method**: `GET`
- **Input Schema**: None
- **Output Schema**:
  ```json
  {
    "timestamp": "ISO-8601",
    "database_stats": {
      "products": "integer",
      "suppliers": "integer",
      "purchase_orders": "integer",
      "stock_movements": "integer",
      "users": "integer",
      "alerts": "integer",
      "total_size_mb": "float",
      "index_size_mb": "float"
    },
    "system_info": {"version": "1.0.0", "environment": "development"}
  }
  ```
- **Status Codes**: `200 OK`, `500 Internal Server Error`

---

## 3. Products Namespace (`/products`)

### GET `/api/products/`
- **Method**: `GET`
- **Query Parameters**:
  - `category` (string, optional)
  - `status` (string, default: `active`)
  - `supplier_id` (string, optional)
  - `low_stock` (boolean, optional)
  - `page` (int, default: 1)
  - `per_page` (int, default: 20)
- **Output Schema**: `{"products": [Product], "pagination": PaginationMeta, "message": "string", "status": "success"}`
- **Status Codes**: `200 OK`, `500 Internal Server Error`

### POST `/api/products/`
- **Method**: `POST`
- **Input Schema**: Product JSON (`name`, `category`, `sku`, `supplier_id`, `current_stock`, `reorder_threshold`, `selling_price`, etc.)
- **Output Schema**: `{"product": Product, "message": "string", "status": "success"}`
- **Status Codes**: `201 Created`, `400 Bad Request`, `500 Internal Server Error`

---

## 4. Suppliers Namespace (`/suppliers`)

### GET `/api/suppliers/`
- **Method**: `GET`
- **Query Parameters**: `status` (default: `active`), `category`, `min_rating`, `page`, `per_page`
- **Output Schema**: `{"suppliers": [Supplier], "pagination": PaginationMeta, "message": "string", "status": "success"}`
- **Status Codes**: `200 OK`

### POST `/api/suppliers/`
- **Method**: `POST`
- **Input Schema**: Supplier JSON (`name`, `contact_email`, `company_name`, `lead_time_days`, etc.)
- **Output Schema**: `{"supplier": Supplier, "message": "string", "status": "success"}`
- **Status Codes**: `201 Created`, `400 Bad Request`

---

## 5. Orders Namespace (`/orders`)

### GET `/api/orders/`
- **Method**: `GET`
- **Query Parameters**: `status`, `supplier_id`, `start_date`, `end_date`, `page`, `per_page`
- **Output Schema**: `{"orders": [Order], "pagination": PaginationMeta, "message": "string", "status": "success"}`
- **Status Codes**: `200 OK`

---

## 6. Alerts Namespace (`/alerts`)

### GET `/api/alerts/`
- **Method**: `GET`
- **Query Parameters**: `status` (default: `active`), `severity`, `type`, `product_id`, `action_required`, `page`, `per_page`
- **Output Schema**: `{"alerts": [Alert], "stats": AlertStats, "pagination": PaginationMeta, "status": "success"}`
- **Status Codes**: `200 OK`

---

## 7. Users Namespace (`/users`)

### GET `/api/users/`
- **Method**: `GET`
- **Query Parameters**: `role`, `status` (default: `active`), `department`, `page`, `per_page`
- **Output Schema**: `{"users": [UserWithoutHash], "stats": UserStats, "pagination": PaginationMeta, "status": "success"}`
- **Status Codes**: `200 OK`

---

## 8. AI & Analytics Namespace (`/ai`)

### GET `/api/ai/forecast/<string:product_id>`
- **Method**: `GET`
- **Query Parameters**: `days_ahead` (int, default: 30)
- **Output Schema**:
  ```json
  {
    "status": "success",
    "product_id": "string",
    "forecast_period_days": 30,
    "ai_forecast": {
      "forecast": {
        "daily_demand": "number",
        "total_demand": "number",
        "confidence_level": "high | medium | low",
        "trend": "increasing | stable | decreasing"
      },
      "insights": ["string"],
      "recommendations": ["string"]
    },
    "statistical_baseline": "object",
    "ai_model": "MiniMax-M1"
  }
  ```
- **Status Codes**: `200 OK`, `500 Internal Server Error`

### GET `/api/ai/analytics/dashboard`
- **Method**: `GET`
- **Query Parameters**: `time_period` (int, default: 30)
- **Output Schema**: `{"status": "success", "dashboard": DashboardData, "timestamp": "ISO-8601"}`
- **Status Codes**: `200 OK`, `500 Internal Server Error`

### GET `/api/ai/health`
- **Method**: `GET`
- **Output Schema**: `{"status": "success", "health_analysis": HealthAnalysis, "key_metrics": [KPI], "timestamp": "ISO-8601"}`
- **Status Codes**: `200 OK`
