# HTTP Request Recipes

These examples describe useful request shapes for exercising an API from the tester UI.

## GET with query parameters

Use a URL such as:

`https://example.com/items?limit=10&offset=0`

This is useful for checking pagination and query parsing.

## JSON POST

Set the method to POST, add a JSON content type header, and provide a small JSON body such as:

`{"name":"demo","enabled":true}`

## Custom headers

Headers such as `Accept`, `Authorization`, and application-specific headers can be tested individually to isolate authentication and content-negotiation issues.

## Debugging tip

When a request fails, compare the status code, response headers, and response body together. A successful HTTP connection does not necessarily mean the API accepted the request.