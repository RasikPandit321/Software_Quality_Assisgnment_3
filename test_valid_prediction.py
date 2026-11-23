"""Test successful prediction using a valid image."""

from pathlib import Path


def test_valid_prediction(client, csrf_token):
    """Verify that uploading a valid image returns a prediction."""

    image_path = next(Path("test_images/5").glob("*.jpeg"))

    with image_path.open("rb") as image_file:
        response = client.post(
            "/prediction",
            data={
                "csrf_token": csrf_token,
                "file": (image_file, image_path.name)
            },
            content_type="multipart/form-data"
        )

    assert response.status_code == 200
    assert b"File cannot be processed." not in response.data
    assert b"5" in response.data
