"""
AI War Room Service - P0 Real-Time AI Command Center
"""
from backend.services.demo_seeder_service import DemoDataSeeder


class WarRoomService:
    """Provides high-priority real-time intelligence feeds, revenue risk metrics, and stockout alerts"""

    @classmethod
    def get_command_center_overview(cls):
        events = DemoDataSeeder.get_50_war_room_events()
        products = DemoDataSeeder.get_100_products()
        suppliers = DemoDataSeeder.get_20_suppliers()

        low_stock_count = sum(1 for p in products if p["is_low_stock"])
        total_rev_risk = sum(p["reorder_quantity"] * p["selling_price"] for p in products if p["is_low_stock"])

        return {
            "summary_metrics": {
                "revenue_at_risk": round(total_rev_risk, 2),
                "potential_stockouts": low_stock_count,
                "critical_suppliers": 3,
                "orders_requiring_attention": 7,
                "ai_confidence_score": 94.8
            },
            "critical_risks": [
                {
                    "id": "RISK-1",
                    "product_name": "Industrial Sensor X200",
                    "sku": "ELEC-SEN-200",
                    "risk_type": "Imminent Stockout",
                    "days_until_stockout": 4,
                    "revenue_impact": 18400.0,
                    "supplier": "Apex Electronics Corp",
                    "recommended_action": "Execute auto-replenishment PO-1042 for 300 units"
                },
                {
                    "id": "RISK-2",
                    "product_name": "Hydraulic Valve V-500",
                    "sku": "MECH-VAL-500",
                    "risk_type": "Supplier Port Delay",
                    "days_until_stockout": 7,
                    "revenue_impact": 12500.0,
                    "supplier": "Midwest Industrial Supply",
                    "recommended_action": "Switch temporary volume to backup supplier SUPP-004"
                },
                {
                    "id": "RISK-3",
                    "product_name": "Microcontroller Unit MCU-32",
                    "sku": "ELEC-MCU-032",
                    "risk_type": "Demand Surge (+42%)",
                    "days_until_stockout": 9,
                    "revenue_impact": 24900.0,
                    "supplier": "Apex Electronics Corp",
                    "recommended_action": "Increase buffer threshold to 85 units"
                }
            ],
            "timeline_feed": events
        }
