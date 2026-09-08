from typing import Any

import httpx
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from app.services.requester import send_request


app = FastAPI(
    title="API Tester",
    description="A lightweight local API testing tool.",
    version="1.0.1",
)


class RequestData(BaseModel):
    method: str = Field(default="GET", min_length=1, max_length=16)
    url: str = Field(min_length=1, max_length=2048)
    headers: dict[str, str] = Field(default_factory=dict)
    params: dict[str, str] = Field(default_factory=dict)
    body: Any | None = None


@app.get("/api/health")
async def health():
    return {"status": "ok", "application": "API Tester"}


@app.post("/api/request")
async def make_request(request: RequestData):
    allowed_methods = {"GET", "POST", "PUT", "PATCH", "DELETE", "HEAD", "OPTIONS"}
    method = request.method.strip().upper()

    if method not in allowed_methods:
        raise HTTPException(status_code=400, detail=f"Unsupported HTTP method: {method}")

    if not request.url.startswith(("http://", "https://")):
        raise HTTPException(status_code=400, detail="URL must start with http:// or https://")

    try:
        return await send_request(
            method=method,
            url=request.url,
            headers=request.headers,
            params=request.params,
            body=request.body,
        )
    except httpx.HTTPError as error:
        raise HTTPException(status_code=502, detail=str(error)) from error
