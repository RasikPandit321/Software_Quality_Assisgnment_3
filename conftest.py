"""Shared pytest fixtures for Flask application tests."""

import re
import pytest
from app import app


@pytest.fixture
def client():
    """Create a Flask test client."""
    with app.test_client() as test_client:
        yield test_client


@pytest.fixture
def csrf_token(client):
    """Retrieve a valid CSRF token from the homepage."""
    response = client.get("/")

    assert response.status_code == 200

    match = re.search(
        rb'name="csrf_token"\s+value="([^"]+)"',
        response.data
    )

    assert match is not None, "CSRF token not found in homepage"

    return match.group(1).decode("utf-8")
