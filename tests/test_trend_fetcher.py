import pytest

def test_trend_data_structure():
    """
    Asserts that the trend data fetched from external MCP resources 
    matches the Project Chimera API contract.
    """
    # This represents the data we EXPECT from our future trend_fetcher skill
    mock_trend_data = {
        "topic": "Autonomous Agents",
        "velocity": 0.85,
        "source": "X_Trends",
        "timestamp": "2026-02-06T12:00:00Z"
    }
    
    # REQUIREMENT: Every trend must have a 'velocity' score (0.0 - 1.0)
    # for the Planner to prioritize tasks.
    assert "velocity" in mock_trend_data
    assert isinstance(mock_trend_data["velocity"], float)
    
    # REQUIREMENT: Must include a source for the Judge to verify authenticity.
    assert "source" in mock_trend_data
    
    # FAIL POINT: Trigger the actual function that doesn't exist yet
    from skills.skill_trend_fetcher import get_latest_trends
    real_data = get_latest_trends() # This will raise an ImportError
    assert real_data == mock_trend_data