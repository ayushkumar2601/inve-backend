"""
Supply Chain Digital Twin Simulation Service - P1
Runs What-If scenarios and provides interactive chart datasets.
"""
from typing import Dict, Any


class SimulationService:
    """Supply Chain Digital Twin What-If Simulator"""

    SCENARIO_LIBRARY = {
        "holiday_rush": {
            "name": "Holiday Rush",
            "demand_increase_pct": 65,
            "supplier_delay_days": 4,
            "lead_time": 11,
            "market_volatility": 35,
            "description": "Simulates peak Q4 retail demand surge alongside carrier shipping bottlenecks."
        },
        "supplier_failure": {
            "name": "Supplier Failure",
            "demand_increase_pct": 10,
            "supplier_delay_days": 18,
            "lead_time": 25,
            "market_volatility": 60,
            "description": "Simulates sudden disruption of a primary Tier-1 supplier manufacturing plant."
        },
        "market_expansion": {
            "name": "Market Expansion",
            "demand_increase_pct": 120,
            "supplier_delay_days": 2,
            "lead_time": 9,
            "market_volatility": 25,
            "description": "Simulates expansion into two new regional sales territories."
        },
        "logistics_crisis": {
            "name": "Logistics Crisis",
            "demand_increase_pct": 0,
            "supplier_delay_days": 14,
            "lead_time": 21,
            "market_volatility": 80,
            "description": "Simulates major maritime canal blockade or cross-border freight strike."
        },
        "product_launch": {
            "name": "Product Launch",
            "demand_increase_pct": 85,
            "supplier_delay_days": 1,
            "lead_time": 7,
            "market_volatility": 40,
            "description": "Simulates initial 30-day demand spike following a major product release."
        }
    }

    @classmethod
    def run_simulation(cls, params: Dict[str, Any]) -> Dict[str, Any]:
        demand_pct = float(params.get("demand_increase_pct", 20))
        delay_days = float(params.get("supplier_delay_days", 3))
        lead_time = float(params.get("lead_time", 7))
        volatility = float(params.get("market_volatility", 25))

        base_rev = 145000.0
        rev_impact = round((demand_pct * 1200) - (delay_days * 3800) - (volatility * 450), 2)
        stockouts = max(0, int((demand_pct / 15) + (delay_days * 0.8)))
        inv_cost = round(35200.0 + (demand_pct * 180) + (delay_days * 310), 2)
        risk_score = min(99, max(12, int((demand_pct * 0.3) + (delay_days * 2.8) + (volatility * 0.4))))

        chart_data = []
        for week in range(1, 13):
            projected_demand = round(100 * (1 + (demand_pct / 100)) * (1 + (week * 0.02)))
            available_stock = max(0, round(500 - (projected_demand * (week * 0.25)) + (150 if week > (lead_time / 7) else 0)))
            chart_data.append({
                "week": f"Week {week}",
                "projected_demand": projected_demand,
                "available_stock": available_stock,
                "safety_buffer": 80
            })

        recommendations = [
            f"Increase safety stock buffer by +{max(10, int(demand_pct * 0.4))}% across critical SKUs",
            f"Pre-order {int((lead_time + delay_days) * 45)} units to hedge against {int(delay_days)}-day supplier delays",
            "Activate secondary regional distributor contract to decouple single-source dependency"
        ]

        return {
            "simulation_output": {
                "revenue_impact": rev_impact,
                "projected_revenue": round(base_rev + rev_impact, 2),
                "stockouts": stockouts,
                "inventory_cost": inv_cost,
                "risk_score": risk_score,
                "recommended_actions": recommendations
            },
            "chart_series": chart_data,
            "scenarios": cls.SCENARIO_LIBRARY
        }
