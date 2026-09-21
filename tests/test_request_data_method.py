from app.main import RequestData

def test_request_data_method_is_preserved():
    request = RequestData(method="POST", url="https://example.com")
    assert request.method == "POST"
