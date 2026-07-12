"""
Enterprise Demo Data Seeder Service for InventoryPulse AI Operations Platform.
Generates comprehensive, realistic enterprise supply chain data.
"""
import random
from datetime import datetime, timedelta

PRODUCT_CATEGORIES = ["Electronics", "Mechanical", "Semiconductors", "Hydraulics", "Optics", "Sensors", "Robotics", "Power Systems"]
SUPPLIER_NAMES = [
    ("Apex Electronics Corp", "Electronics"),
    ("Midwest Industrial Supply", "Mechanical"),
    ("Nexus Semiconductor Labs", "Semiconductors"),
    ("Vanguard Hydraulics Inc", "Hydraulics"),
    ("AeroPrecision Systems", "Robotics"),
    ("Quantum Silicon AG", "Semiconductors"),
    ("Titanium Forge Co", "Mechanical"),
    ("Omno-Sensor Technologies", "Sensors"),
    ("Helios Optics Ltd", "Optics"),
    ("Pacific Power & Grid", "Power Systems"),
    ("Kyoto Micro-Devices", "Electronics"),
    ("Nordic Automation Dynamics", "Robotics"),
    ("Silicon Valley Wafer Fab", "Semiconductors"),
    ("Bavarian Precision Gears", "Mechanical"),
    ("Alpine Cryo-Cooling", "Power Systems"),
    ("Global Connectors Inc", "Electronics"),
    ("Zenith Photonics Group", "Optics"),
    ("Atlas Servo Components", "Robotics"),
    ("Starlight Circuitry", "Electronics"),
    ("Orbital Pneumatics LLC", "Hydraulics")
]

PRODUCT_ADJECTIVES = ["Industrial", "Ultra-Precision", "Heavy-Duty", "Quantum", "High-Speed", "Micro", "Advanced", "Modular", "Smart", "Rugged"]
PRODUCT_NOUNS = ["Sensor", "Microcontroller", "Hydraulic Valve", "Optical Diode", "Actuator", "Power Inverter", "Processor Array", "Servo Motor", "Cryo-Pump", "Transceiver"]


class DemoDataSeeder:
    """Generates deterministic, highly realistic enterprise datasets"""
    
    @classmethod
    def get_100_products(cls):
        products = []
        random.seed(42)
        for i in range(1, 101):
            category = random.choice(PRODUCT_CATEGORIES)
            adj = random.choice(PRODUCT_ADJECTIVES)
            noun = random.choice(PRODUCT_NOUNS)
            sku = f"{category[:4].upper()}-{i:03d}"
            name = f"{adj} {noun} {sku}"
            supp_id = f"SUPP-{((i - 1) % 20) + 1:03d}"
            current_stock = round(random.uniform(5, 500), 1)
            threshold = round(random.uniform(15, 80), 1)
            cost = round(random.uniform(10, 450), 2)
            selling = round(cost * random.uniform(1.4, 2.5), 2)
            is_low = current_stock <= threshold
            products.append({
                "product_id": f"PROD-{i:03d}",
                "name": name,
                "category": category,
                "sku": sku,
                "supplier_id": supp_id,
                "current_stock": current_stock,
                "reorder_threshold": threshold,
                "reorder_quantity": round(threshold * 3),
                "cost_price": cost,
                "selling_price": selling,
                "status": "active",
                "is_low_stock": is_low,
                "stock_status": "low_stock" if is_low else "healthy",
                "description": f"Enterprise grade {name.lower()} for high-reliability manufacturing pipelines."
            })
        return products

    @classmethod
    def get_20_suppliers(cls):
        suppliers = []
        for idx, (name, cat) in enumerate(SUPPLIER_NAMES, start=1):
            suppliers.append({
                "supplier_id": f"SUPP-{idx:03d}",
                "name": name,
                "company_name": name,
                "contact_email": f"orders@{name.lower().replace(' ', '')}.com",
                "contact_phone": f"+1-555-01{idx:02d}",
                "lead_time_days": random.randint(5, 21),
                "rating": round(random.uniform(4.1, 4.9), 1),
                "risk_tier": "low" if idx % 4 != 0 else ("medium" if idx % 2 == 0 else "high"),
                "status": "active",
                "categories": [cat]
            })
        return suppliers

    @classmethod
    def get_50_war_room_events(cls):
        events = []
        now = datetime.utcnow()
        products = cls.get_100_products()
        reasons = [
            ("Demand spike detected", "Stockout predicted in 6 days", 18400, "Order 500 units immediately"),
            ("Supplier port bottleneck reported", "Lead time increased by +5 days", 24200, "Route backup order via Midwest Industrial"),
            ("Unusual inventory drainage", "Stock fell below critical threshold", 14500, "Expedite shipment via air freight"),
            ("Forecast anomaly flagged", "Seasonality multiplier +45%", 31200, "Increase safety stock by 25%"),
            ("Quality SLA breach risk", "Yield variance exceeded 3.2%", 9800, "Initiate supplier lot inspection")
        ]
        for idx in range(1, 51):
            prod = products[idx % len(products)]
            reason, impact, rev_risk, action = reasons[idx % len(reasons)]
            ts = (now - timedelta(minutes=idx * 27)).strftime("%H:%M")
            events.append({
                "id": f"WR-EVT-{idx:03d}",
                "time": ts,
                "timestamp": (now - timedelta(minutes=idx * 27)).isoformat() + "Z",
                "event_type": reason,
                "product_id": prod["product_id"],
                "product_name": prod["name"],
                "impact": impact,
                "revenue_risk": rev_risk + (idx * 150),
                "recommendation": action,
                "severity": "critical" if idx % 5 == 0 else ("high" if idx % 2 == 0 else "medium"),
                "confidence_score": 88 + (idx % 11)
            })
        return events

    @classmethod
    def get_100_agent_activities(cls):
        activities = []
        now = datetime.utcnow()
        agents = ["Forecast Agent", "Risk Agent", "Supplier Agent", "Procurement Agent", "Finance Agent"]
        actions = [
            ("Forecast Agent", "Predicted stockout for PROD-014", "94% confidence", "Identified 8-day buffer deficit"),
            ("Risk Agent", "Revenue impact estimated at $18,400", "High Risk", "Escalated to Autonomous Procurement pipeline"),
            ("Supplier Agent", "Selected Supplier Apex Electronics (SUPP-001)", "SLA 99.1%", "Verified 7-day expedited lead time"),
            ("Procurement Agent", "Generated automated PO-1042", "Auto-Approved", "Transmitted EDI order for 350 units"),
            ("Finance Agent", "Working capital allocation optimized", "ROI +14.2%", "Rebalanced cash buffer across tier-1 SKUs")
        ]
        for idx in range(1, 101):
            agent, title, metric, detail = actions[idx % len(actions)]
            ts = (now - timedelta(minutes=idx * 14)).strftime("%H:%M:%S")
            activities.append({
                "id": f"ACT-{idx:03d}",
                "timestamp": ts,
                "agent_name": agent,
                "action_title": f"{title} (#{idx})",
                "metric": metric,
                "detail": detail,
                "status": "completed"
            })
        return activities
