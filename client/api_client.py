import requests
from typing import Dict, Any, Optional, List


class UserApiClient:
    def __init__(self, base_url: str, timeout: Optional[int] = 10):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

    def _request(self, method: str, endpoint: str, **kwargs) -> Any:
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        try:
            response = requests.request(method, url, timeout=self.timeout, **kwargs)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            if response.status_code == 400:
                raise ValueError(f"Bad Request: {response.json().get('detail')}")
            elif response.status_code == 404:
                raise ValueError("Resource not found")
            raise e
        except requests.exceptions.RequestException as e:
            raise ConnectionError(f"Failed to connect to {url}: {str(e)}")

    def health_check(self) -> Dict[str, Any]:
        return self._request("GET", "/health")

    def create_user(self, user_data: Dict[str, Any]) -> Dict[str, Any]:
        return self._request("POST", "/users", json=user_data)

    def get_user(self, user_id: str) -> Dict[str, Any]:
        return self._request("GET", f"/users/{user_id}")

    def list_users(self) -> List[str]:
        return self._request("GET", "/users")
