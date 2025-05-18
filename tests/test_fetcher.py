import pytest
from weather.fetcher import get_weather

def test_get_weather(monkeypatch):
    class MockResponse:
        def raise_for_status(self): pass
        def json(self):
            return {
                "name": "Lagos",
                "main": {"temp": 30},
                "weather": [{"description": "sunny"}]
            }

    monkeypatch.setattr("requests.get", lambda *args, **kwargs: MockResponse())
    result = get_weather("Lagos", "dummy_key")
    assert result["city"] == "Lagos"
    assert result["temp"] == 30
    assert result["description"] == "sunny"
