def test_secret_endpoint(client):
    response = client.get("/secret")
    assert response.status_code == 200
    assert "secret_code" in response.json
    