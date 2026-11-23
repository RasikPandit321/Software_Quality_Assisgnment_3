"""Acceptance test for missing image uploads."""


def test_acceptance_missing_file(client, csrf_token):
    """Verify that an upload without a file shows an error message."""

    response = client.post(
        "/prediction",
        data={"csrf_token": csrf_token},
        content_type="multipart/form-data"
    )

    assert response.status_code == 200
    assert b"File cannot be processed" in response.data
