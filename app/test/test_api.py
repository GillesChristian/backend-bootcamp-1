from starlette.testclient import TestClient

from main import create_app

app = create_app()

client = TestClient(app)

def test_get_students():
    response = client.get("/api/students")
    print(response.status_code)
    assert response.status_code == 200
    
test_get_students()