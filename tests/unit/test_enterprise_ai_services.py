"""
Unit tests for InventoryPulse AI Operations Platform Services
"""
import pytest
from backend.services.demo_seeder_service import DemoDataSeeder
from backend.services.war_room_service import WarRoomService
from backend.services.copilot_service import CopilotService
from backend.services.procurement_agent_service import ProcurementAgentService
from backend.services.simulation_service import SimulationService
from backend.services.agent_orchestrator_service import AgentOrchestratorService


def test_demo_data_seeder():
    products = DemoDataSeeder.get_100_products()
    assert len(products) == 100
    suppliers = DemoDataSeeder.get_20_suppliers()
    assert len(suppliers) == 20
    events = DemoDataSeeder.get_50_war_room_events()
    assert len(events) >= 50
    activities = DemoDataSeeder.get_100_agent_activities()
    assert len(activities) >= 100


def test_war_room_service():
    overview = WarRoomService.get_command_center_overview()
    assert "summary_metrics" in overview
    assert "critical_risks" in overview
    assert "timeline_feed" in overview
    assert len(overview["timeline_feed"]) >= 50
    assert overview["summary_metrics"]["ai_confidence_score"] > 0


def test_copilot_service():
    res1 = CopilotService.analyze_query("Why did inventory costs increase?")
    assert "root_cause" in res1
    assert "recommended_action" in res1
    assert res1["confidence_score"] > 0

    res2 = CopilotService.analyze_query("Custom question about logistics")
    assert "root_cause" in res2
    assert "confidence_score" in res2


def test_procurement_agent_service():
    dashboard = ProcurementAgentService.get_procurement_dashboard()
    assert "active_workflows" in dashboard
    assert len(dashboard["activity_timeline"]) >= 100


def test_simulation_service():
    result = SimulationService.run_simulation({
        "demand_increase_pct": 50,
        "supplier_delay_days": 5
    })
    assert "simulation_output" in result
    assert "chart_series" in result
    assert len(result["chart_series"]) == 12
    assert "scenarios" in result
    assert len(result["scenarios"]) == 5


def test_agent_orchestrator_service():
    network = AgentOrchestratorService.get_agent_network_status()
    assert "agents" in network
    assert len(network["agents"]) == 5
    assert "communication_graph" in network
