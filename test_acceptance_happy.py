"""Acceptance tests for successful image uploads."""

from io import BytesIO


def test_acceptance_successful_upload(client, csrf_token):
    """Test uploading an image file."""
    img_data = BytesIO(b"fake_image_data")
    img_data.name = "test_image.jpg"

    response = client.post(
        "/prediction",
        data={
            "csrf_token": csrf_token,
            "file": (img_data, img_data.name)
        },
        content_type="multipart/form-data"
    )

    assert response.status_code == 200
    assert b"Prediction" in response.data


def test_acceptance_valid_large_image(client, csrf_token):
    """Test uploading an image within the allowed size."""
    img_data = BytesIO(b"fake_large_image_data" * 1000)
    img_data.name = "large_image.jpg"

    response = client.post(
        "/prediction",
        data={
            "csrf_token": csrf_token,
            "file": (img_data, img_data.name)
        },
        content_type="multipart/form-data"
    )

    assert response.status_code == 200
    assert b"Prediction" in response.data


def test_acceptance_valid_image_size_upload(client, csrf_token):
    """Test uploading an image with a specific size."""
    img_data = BytesIO(b"valid_image_data_of_large_size" * 1000)
    img_data.name = "large_image.jpg"

    response = client.post(
        "/prediction",
        data={
            "csrf_token": csrf_token,
            "file": (img_data, img_data.name)
        },
        content_type="multipart/form-data"
    )

    assert response.status_code == 200
    assert b"Prediction" in response.data
