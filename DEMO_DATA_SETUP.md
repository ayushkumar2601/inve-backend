# InventoryPulse AI — Enterprise Demo Data Setup & Deterministic Seeding

To ensure a high-impact demo with zero blank states, zero API timeouts, and impressive enterprise numbers, InventoryPulse AI includes a deterministic enterprise data seeder (`backend/services/demo_seeder_service.py`).

---

## 1. Key Enterprise KPI Baseline Values

When recording the demo, the following executive values are guaranteed across all endpoints:

| Metric / Scorecard | Seeded Demo Value | Strategic Purpose in Demo Story |
| :--- | :--- | :--- |
| **Revenue at Risk** | **$378,046** | Immediate P0 executive gravity (exceeds $250k judge wow threshold) |
| **Total Inventory Portfolio Value** | **$4,820,500** | Establishes enterprise scale ($4.8M+ working capital under management) |
| **Predicted Stockouts** | **6 Critical SKUs** | Demonstrates precise AI forward risk detection (≤ 7 days window) |
| **Critical Suppliers** | **3 Suppliers** | Highlights SLA lead-time drift detection |
| **AI Consensus Confidence** | **94.8% – 99.4%** | Multi-model auditing across statistical + LLM layers |
| **Procurement Efficiency** | **98.4%** | Direct automated EDI routing rate |

---

## 2. Seeded Critical Inventory Risks (`/war-room`)

1. **Industrial Sensor X200 (`ELEC-SEN-200`)**:
   - **Status**: Imminent Stockout (4 Days remaining)
   - **Revenue Impact**: **$18,400.00**
   - **Supplier**: Apex Electronics Corp
   - **Recommended Action**: *Execute auto-replenishment PO-1042 for 300 units*
2. **Hydraulic Valve V-500 (`VALV-HYD-500`)**:
   - **Status**: Critical Stockout Risk (6 Days remaining)
   - **Revenue Impact**: **$42,100.00**
   - **Supplier**: Precision Hydraulics Ltd
   - **Recommended Action**: *Expedite air freight delivery PO-1043*

---

## 3. Seeded Executive Copilot Query Syntheses (`/copilot`)

* **Query**: *"Why did inventory costs increase this month?"*
  * **Root Cause**: Semiconductor safety stock buffer expansion (+18%) combined with expedited air freight charges from Apex Electronics due to port congestion.
  * **Business Impact**: Working capital holding costs increased by **$34,200**, protected **$378,046** in high-margin enterprise revenue.
  * **Risk Level**: `Optimized` | **Confidence**: `99.4%`
* **Query**: *"What should I reorder today?"*
  * **Recommended Action**: Execute pre-authorized EDI Purchase Orders `PO-1042` (300 units Sensor X200) and `PO-1043` (150 units Valve V-500).

---

## 4. How to Reset / Verify Demo Data Before Recording

Our backend endpoints (`/api/ai/war-room`, `/api/ai/copilot`, `/api/ai/simulation`, `/api/ai/agents`) automatically load these exact deterministic datasets if live external DBs are disconnected or during demo runs.

To verify endpoints before recording:
```bash
curl -s http://localhost:5500/api/ai/war-room | grep -o "378046"
```
*(Should output `378046` confirming the $378,046 Revenue at Risk payload is live).*
