
import httpx


async def send_request(
    method: str,
    url: str,
    headers: dict | None = None,
    params: dict | None = None,
    body: object | None = None,
) -> dict:
    async with httpx.AsyncClient(
        timeout=30.0,
        follow_redirects=True,
    ) as client:
        response = await client.request(
            method=method.upper(),
            url=url,
            headers=headers or {},
            params=params or {},
            json=body,
        )

        try:
            data = response.json()
        except ValueError:
            data = response.text

        return {
            "status_code": response.status_code,
            "reason": response.reason_phrase,
            "headers": dict(response.headers),
            "body": data,
        }
