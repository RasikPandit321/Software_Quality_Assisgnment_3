"""Test how the Flask application handles missing uploads."""


def test_missing_file_upload(client, csrf_token):
    """Verify that submitting without a file displays an error."""

    response = client.post(
        "/prediction",
        data={"csrf_token": csrf_token},
        content_type="multipart/form-data"
    )

    assert response.status_code == 200
    assert b"File cannot be processed." in response.data
