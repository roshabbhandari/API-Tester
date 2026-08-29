
import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_health():
response = client.get("/api/health")

```
assert response.status_code == 200
assert response.json()["status"] == "ok"
assert response.json()["application"] == "API Tester"
```

def test_invalid_method():
response = client.post(
"/api/request",
json={
"method": "INVALID",
"url": "https://httpbin.org/get",
},
)

```
assert response.status_code == 400
assert "Unsupported HTTP method" in response.json()["detail"]
```

def test_invalid_url():
response = client.post(
"/api/request",
json={
"method": "GET",
"url": "invalid-url",
},
)

```
assert response.status_code == 400
assert "http://" in response.json()["detail"]
```

def test_request_schema():
response = client.post(
"/api/request",
json={
"method": "GET",
"url": "https://httpbin.org/get",
"headers": {},
"params": {},
"body": None,
},
)

```
assert response.status_code in (200, 502)
```

@pytest.mark.parametrize(
"method",
["GET", "POST", "PUT", "PATCH", "DELETE"],
)
def test_supported_methods(method):
response = client.post(
"/api/request",
json={
"method": method,
"url": "https://httpbin.org",
},
)

```
assert response.status_code in (200, 502)
```
