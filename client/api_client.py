import requests

class UserApiClient:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")

    def health_check(self):
        response = requests.get(f"{self.base_url}/health")
        response.raise_for_status()
        return response.json()

    def create_user(self, user_data: dict):
        response = requests.post(f"{self.base_url}/users", json=user_data)
        if response.status_code == 400:
            raise ValueError(f"User creation failed: {response.json()['detail']}")
        response.raise_for_status()
        return response.json()

    def get_user(self, user_id: str):
        response = requests.get(f"{self.base_url}/users/{user_id}")
        if response.status_code == 404:
            raise ValueError("User not found")
        response.raise_for_status()
        return response.json()

    def list_users(self):
        response = requests.get(f"{self.base_url}/users")
        response.raise_for_status()
        return response.json()
