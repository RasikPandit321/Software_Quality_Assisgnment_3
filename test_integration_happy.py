"""Integration test for successful image prediction."""

from io import BytesIO


def test_successful_prediction(client, csrf_token):
    """Test image upload and prediction with CSRF protection."""

    img_data = BytesIO(b"fake_image_data")
    img_data.name = "test.jpg"

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
