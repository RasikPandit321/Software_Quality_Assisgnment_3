"""Tests for invalid image uploads."""

from io import BytesIO


def test_invalid_image_upload(client, csrf_token):
    """Verify that invalid image data produces an error message."""

    invalid_file = BytesIO(b"This is not a valid image.")

    response = client.post(
        "/prediction",
        data={
            "csrf_token": csrf_token,
            "file": (invalid_file, "invalid.jpg")
        },
        content_type="multipart/form-data"
    )

    assert response.status_code == 200
    assert b"File cannot be processed." in response.data
