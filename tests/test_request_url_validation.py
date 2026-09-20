import pytest
from fastapi import HTTPException
from app.main import RequestData, make_request


@pytest.mark.asyncio
async def test_missing_http_scheme_is_rejected():
    request = RequestData(url='example.com/api')
    with pytest.raises(HTTPException) as error:
        await make_request(request)
    assert error.value.status_code == 400
    assert 'http://' in error.value.detail
