def test_health_endpoint(client):
    """
    Ensure the /health endpoint returns status 200 and contains 'healthy' in the response.
    """
    response = client.get("/health")
    assert response.status_code == 200
    assert "healthy" in response.json["status"]
