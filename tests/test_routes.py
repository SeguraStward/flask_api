import json
import unittest
from unittest.mock import patch
import requests

from app import create_app
from config import Config


class TestConfig(Config):
    TESTING = True


class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.client = self.app.test_client()

    def test_home_endpoint(self):
        """Test the home endpoint returns correct response"""
        response = self.client.get("/api/")
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertIn("message", data)
        self.assertIn("endpoints", data)
        self.assertIn("users", data["endpoints"])

    @patch("app.services.user_service.requests.get")
    def test_users_endpoint_success(self, mock_get):
        """Test the users endpoint returns users when API call succeeds"""
        # Mock API response
        mock_response = unittest.mock.Mock()
        mock_response.json.return_value = {"results": [{"name": "Test User"}]}
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        response = self.client.get("/api/users")
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["name"], "Test User")

    @patch("app.services.user_service.requests.get")
    def test_users_endpoint_api_error(self, mock_get):
        """Test error handling when external API fails"""
        mock_get.side_effect = requests.RequestException("API connection error")

        response = self.client.get("/api/users")
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 503)  # Service Unavailable
        self.assertIn("error", data)


if __name__ == "__main__":
    unittest.main()
