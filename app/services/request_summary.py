from .url_masking import mask_url_credentials


def summarize_request(method: str, url: str) -> str:
    return f"{method.upper()} {mask_url_credentials(url)}"
