import httpx


def describe_http_error(error: httpx.HTTPError) -> str:
    if isinstance(error, httpx.TimeoutException):
        return "Request timed out"
    if isinstance(error, httpx.ConnectError):
        return "Unable to connect to the target host"
    if isinstance(error, httpx.TooManyRedirects):
        return "Too many redirects"
    return str(error) or error.__class__.__name__
