import requests
from flask import current_app
from app.utils.errors import ExternalAPIError


class UserService:
    @staticmethod
    def get_random_users():
        """
        Retrieves 75 random users directly from the external API.
        No local storage is used.
        """
        try:
            # Make a direct request to fetch users
            response = requests.get(
                current_app.config["RANDOM_USER_API_URL"],
                params={"results": current_app.config["USERS_TO_RETURN"]},
                timeout=10,
            )
            response.raise_for_status()

            # Get user data
            return response.json()["results"]

        except requests.RequestException as e:
            current_app.logger.error(f"API request failed: {str(e)}")
            raise ExternalAPIError(f"Error fetching users from external API: {str(e)}")
        except (KeyError, ValueError) as e:
            current_app.logger.error(f"Invalid API response format: {str(e)}")
            raise ExternalAPIError("Invalid response format from external API")
