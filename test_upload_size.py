"""Test whether oversized file uploads are rejected."""

from io import BytesIO


def test_oversized_file_upload(client):
    """Verify uploads larger than 5 MB are rejected."""

    large_file = BytesIO(b"A" * (6 * 1024 * 1024))

    response = client.post(
        "/prediction",
        data={"file": (large_file, "large.jpg")},
        content_type="multipart/form-data"
    )

    assert response.status_code == 413
