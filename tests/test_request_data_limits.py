import pytest
from pydantic import ValidationError

from app.main import RequestData


def test_request_data_rejects_empty_url():
    with pytest.raises(ValidationError):
        RequestData(url="")


def test_request_data_rejects_overlong_method():
    with pytest.raises(ValidationError):
        RequestData(method="X" * 17, url="https://example.com")
