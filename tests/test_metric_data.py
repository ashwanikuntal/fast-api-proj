from fastapi.testclient import TestClient
from fastapi import status
import json
from main import app

client = TestClient(app)

def test_get_all_metrics_data():
    response = client.get("/metrics")
    response_json = json.loads(response.content)
    assert response.status_code == status.HTTP_200_OK
    assert len(response_json) > 0


def test_get_all_metrics_data_after_start_date():
    response = client.get("/metrics?start=2021-04-20")
    response_json = json.loads(response.content)
    assert response.status_code == status.HTTP_200_OK
    assert len(response_json) > 0


def test_get_all_metrics_data_before_end_date():
    response = client.get("/metrics?end=2021-04-22")
    response_json = json.loads(response.content)
    assert response.status_code == status.HTTP_200_OK
    assert len(response_json) > 0


def test_add_metric_data():
    response = client.post(
        "/addMetrics/",
        json={
            "metric": [
                {
                    "created_time": "2021-04-21 17:28:35.173768",
                    "voltage": 195,
                    "current": 4
                }
            ]
        }
    )
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == {"message": "SUCCESS"}


def test_add_metric_data_with_wrong_input():
    response = client.post(
        "/addMetrics/",
        json={
            "metric": [
                {
                    "created_time": "invalid_input",
                    "voltage": 195,
                    "current": 4
                }
            ]
        }
    )
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert response.json() == {"message": "SUCCESS"} 