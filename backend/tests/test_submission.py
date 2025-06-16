import os
import sys
import pytest
from fastapi.testclient import TestClient

# Ensure the src directory is in the path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from main import app

client = TestClient(app)

@ pytest.fixture(autouse=True)
def clear_data_file(tmp_path, monkeypatch):
    """
    Change the working directory to a temporary path for isolation. This ensures submissions.json is created in tmp path.
    """
    monkeypatch.chdir(tmp_path)
    yield


def test_submit_and_export_and_clustering():
    payload = {
        "name": "John Doe",
        "dob": "1990-01-01",
        "email": "john@example.com",
        "phone": "1234567890",
        "injuries": "",
        "medications": "",
        "painPoints": "",
        "historyTypes": ["strength"],
        "historyMotivation": "Stay healthy",
        "goals": ["strength"],
        "vo2Test": "running",
        "vo2Result": "50",
        "vo2Group": "elite",
        "reflectMotivation": "I want to improve",
        "reflectReaction": "Happy",
        "reflectUse": "Will train hard",
        "reflectPrioritize": True
    }
    # Submit form data
    response = client.post("/submit-form-data", json=payload)
    assert response.status_code == 201
    assert response.json() == {"message": "Form data saved"}

    # Export data and verify content
    response = client.get("/export-data")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 1
    entry = data[0]
    assert entry["name"] == "John Doe"
    assert entry["vo2Result"] == "50"

    # Trigger clustering and verify response
    response = client.post("/trigger-clustering")
    assert response.status_code == 200
    result = response.json()
    assert "clusters" in result
    clusters = result["clusters"]
    assert isinstance(clusters, list)
    assert len(clusters) == 1
    assert isinstance(clusters[0], int)
