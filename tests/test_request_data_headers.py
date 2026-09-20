from request_data import RequestData


def test_request_data_preserves_headers_and_params():
    request = RequestData(
        url="https://example.com/api",
        headers={"Accept": "application/json"},
        params={"page": "1"},
    )
    assert request.headers == {"Accept": "application/json"}
    assert request.params == {"page": "1"}
