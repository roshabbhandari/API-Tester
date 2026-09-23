# Testing Strategy

API Tester should test both the request-handling layer and the user-visible response formatting.

## Request behavior

Tests should cover:

- Supported HTTP methods.
- Query strings and request bodies.
- Custom headers.
- Invalid or missing input.
- Timeout and upstream failure handling.

## Response behavior

Tests should verify that the application preserves the important parts of an API response, including status code, headers, and readable body formatting.

## Regression rule

Every bug that changes request or response behavior should add a focused regression test. Keep tests small so a failure identifies one behavior rather than an entire workflow.

For local development, run the existing test suite before opening a pull request.