from app.main import RequestData


def test_request_data_defaults_method_and_collections():
    request = RequestData(url="https://example.com")
    assert request.method == "GET"
    assert request.headers == {}
    assert request.params == {}
    assert request.body is None
