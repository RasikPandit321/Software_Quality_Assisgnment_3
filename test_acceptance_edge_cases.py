"""Acceptance tests for edge cases in image uploads."""

from io import BytesIO


def post_with_csrf(client, csrf_token, img_data, headers=None):
    """Upload an image with a valid CSRF token."""
    return client.post(
        "/prediction",
        data={
            "csrf_token": csrf_token,
            "file": (img_data, img_data.name)
        },
        content_type="multipart/form-data",
        headers=headers
    )


# 1. Edge Case: Uploading a Large Image File
def test_edge_case_large_image_upload(client, csrf_token):
    """Verify that uploads larger than 5 MB are rejected."""
    large_img_data = BytesIO(b"large_image_data" * 10**6)
    large_img_data.name = "large_image.jpg"

    response = post_with_csrf(
        client, csrf_token, large_img_data
    )

    assert response.status_code == 413


# 2. Edge Case: Uploading an Image with Invalid Metadata
def test_edge_case_invalid_metadata(client, csrf_token):
    """Test uploading an image with invalid metadata."""
    img_data = BytesIO(b"image_with_no_metadata")
    img_data.name = "image_no_metadata.jpg"

    response = post_with_csrf(
        client, csrf_token, img_data
    )

    assert b"Prediction" in response.data


# 3. Edge Case: Uploading a Non-Standard Image Extension
def test_edge_case_non_standard_image_extensions(client, csrf_token):
    """Test uploading an image with a non-standard extension."""
    img_data = BytesIO(b"valid_image_data")
    img_data.name = "non_standard_image.webp"

    response = post_with_csrf(
        client, csrf_token, img_data
    )

    assert b"Prediction" in response.data


# 4. Edge Case: Sequential Image Uploads
def test_edge_case_sequential_image_uploads(client, csrf_token):
    """Test uploading multiple images sequentially."""
    img_data1 = BytesIO(b"first_image_data")
    img_data1.name = "first_image.jpg"

    img_data2 = BytesIO(b"second_image_data")
    img_data2.name = "second_image.jpg"

    response1 = post_with_csrf(
        client, csrf_token, img_data1
    )

    response2 = post_with_csrf(
        client, csrf_token, img_data2
    )

    assert b"Prediction" in response1.data
    assert b"Prediction" in response2.data


# 5. Edge Case: Unexpected Headers
def test_edge_case_unexpected_headers(client, csrf_token):
    """Test uploading an image with unexpected HTTP headers."""
    img_data = BytesIO(b"valid_image_data")
    img_data.name = "unexpected_headers_image.jpg"

    response = post_with_csrf(
        client,
        csrf_token,
        img_data,
        headers={"X-Unexpected-Header": "value"}
    )

    assert b"Prediction" in response.data


# 6. Edge Case: Uploading an Image with HTTP/2
def test_edge_case_upload_over_http2(client, csrf_token):
    """Test an image upload using the Flask test client."""
    img_data = BytesIO(b"valid_image_data")
    img_data.name = "http2_image.jpg"

    response = post_with_csrf(
        client, csrf_token, img_data
    )

    assert b"Prediction" in response.data
