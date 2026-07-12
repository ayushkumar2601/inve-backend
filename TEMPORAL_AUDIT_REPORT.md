# InventoryPulse Temporal Workflow Audit Report

## Executive Summary
This document audits the Temporal durable execution orchestration service (`backend/services/temporal_service.py` -> `TemporalInventoryService`). Temporal provides fault-tolerant, multi-step asynchronous workflow automation for background inventory monitoring, restock ordering, and anomaly detection.

---

## 1. Workflows & Activities Registry

### Workflows
1. **`InventoryMonitoringWorkflow`**
   - **Purpose**: Continuously monitors inventory levels across all active products at configurable intervals (`check_interval_seconds`).
   - **Execution Model**: Durable loop using `workflow.sleep()`.
   - **Triggered Activities**: `check_inventory_levels`, `send_alert_activity`.

2. **`RestockWorkflow`**
   - **Purpose**: End-to-end automated replenishment pipeline triggered when an item breaches its reorder threshold.
   - **Execution Sequence**:
     1. Executes `generate_forecast_activity` to compute 30-day predicted demand.
     2. Executes `create_restock_order_activity` to generate a purchase order document in MongoDB.
     3. Executes `send_alert_activity` to notify procurement managers.

3. **`AnomalyDetectionWorkflow`**
   - **Purpose**: Runs periodic data integrity and anomaly audits across operational collections.
   - **Detection Logic**: Flags negative stock counts, extreme stock accumulation, or sudden unexplained zeroing of stock.

4. **`AlertProcessingWorkflow`**
   - **Purpose**: Manages lifecycle escalation of unacknowledged high-priority alerts.

---

## 2. Temporal Activities Implementation Status
| Activity Name | Target Service | Status | Description |
| :--- | :--- | :--- | :--- |
| `check_inventory_levels` | MongoDB Atlas (`products`) | **REAL** | Queries active products where `current_stock <= reorder_threshold`. |
| `generate_forecast_activity` | `AIForecastingService` | **REAL** | Invokes async MiniMax AI forecast and returns structured prediction dictionary. |
| `create_restock_order_activity` | MongoDB Atlas (`purchase_orders`) | **REAL** | Inserts purchase order document with status `pending`. |
| `send_alert_activity` | MongoDB Atlas (`alerts`) | **REAL** | Inserts structured system alert and logs event. |

---

## 3. Configuration & Graceful Fallback
- **Endpoint**: Configured via `TEMPORAL_GRPC_ENDPOINT` (default: `localhost:7233`).
- **Resilience**: If a local Temporal Server is not running during local hackathon execution, `TemporalInventoryService` wraps connection calls in `try/except` blocks, logging warnings while allowing the Flask REST API and core application to continue running without crash.
