"""Integration test for missing image uploads."""


def test_missing_file(client, csrf_token):
    """Verify that a missing file is handled with a valid CSRF token."""

    response = client.post(
        "/prediction",
        data={"csrf_token": csrf_token},
        content_type="multipart/form-data"
    )

    assert response.status_code == 200
    assert b"File cannot be processed." in response.data
