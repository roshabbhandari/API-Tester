from app.main import RequestData


def test_request_data_accepts_structured_body():
    body = {'name': 'Rosenix', 'enabled': True}
    request = RequestData(url='https://example.com', body=body)
    assert request.body == body


def test_request_data_defaults_are_independent():
    first = RequestData(url='https://example.com')
    second = RequestData(url='https://example.com')
    first.headers['X-Test'] = '1'
    assert second.headers == {}
