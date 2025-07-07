def test_secret_endpoint(client):
    """
    Ensure the /secret endpoint returns status 200 and contains 'secret_code' in the response.
    """
    response = client.get("/secret")
    assert response.status_code == 200
    assert "secret_code" in response.json
