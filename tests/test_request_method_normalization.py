import pytest
from fastapi import HTTPException
from app.main import RequestData, make_request


def test_request_data_preserves_method_case():
    request = RequestData(method='post', url='https://example.com')
    assert request.method == 'post'


@pytest.mark.asyncio
async def test_unsupported_method_is_rejected():
    request = RequestData(method='TRACE', url='https://example.com')
    with pytest.raises(HTTPException) as error:
        await make_request(request)
    assert error.value.status_code == 400
