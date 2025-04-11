import unittest
from unittest.mock import patch, Mock

from flask import Flask

from app.services.user_service import UserService
from app.utils.errors import ExternalAPIError


class TestUserService(unittest.TestCase):
    def setUp(self):
        # Create test Flask app context
        self.app = Flask(__name__)
        self.app.config["RANDOM_USER_API_URL"] = "https://randomuser.me/api/"
        self.app.config["USERS_TO_RETURN"] = 5
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    @patch("app.services.user_service.requests.get")
    def test_get_random_users_success(self, mock_get):
        """Test successful API response handling"""
        # Mock successful response
        mock_response = Mock()
        mock_response.json.return_value = {"results": [{"name": "John Doe"}]}
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        # Call the method
        result = UserService.get_random_users()

        # Assertions
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["name"], "John Doe")
        mock_get.assert_called_once()

    @patch("app.services.user_service.requests.get")
    def test_get_random_users_api_error(self, mock_get):
        """Test handling of API request error"""
        import requests

        # Mock request exception
        mock_get.side_effect = requests.RequestException("API connection error")

        # Call the method and check for exception
        with self.assertRaises(ExternalAPIError):
            UserService.get_random_users()


if __name__ == "__main__":
    unittest.main()
