"""Security tests for CSRF protection."""


def test_missing_csrf_token(client):
    """Verify that requests without CSRF tokens are rejected."""

    response = client.post(
        "/prediction",
        data={},
        content_type="multipart/form-data"
    )

    assert response.status_code == 400


def test_invalid_csrf_token(client):
    """Verify that invalid CSRF tokens are rejected."""

    response = client.post(
        "/prediction",
        data={"csrf_token": "invalid-token"},
        content_type="multipart/form-data"
    )

    assert response.status_code == 400


def test_valid_csrf_token(client, csrf_token):
    """Verify that requests with valid CSRF tokens are accepted."""

    response = client.post(
        "/prediction",
        data={"csrf_token": csrf_token},
        content_type="multipart/form-data"
    )

    assert response.status_code == 200
    assert b"File cannot be processed" in response.data
