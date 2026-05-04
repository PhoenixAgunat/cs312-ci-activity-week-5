# Name: Phoenix Agunat
# Date: 5/3/2026
# Activity: Week 5 activity 2

from app import app

def test_index():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert response.get_json()["status"] == "ok"