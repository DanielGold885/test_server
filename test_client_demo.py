from client.api_client import UserApiClient
import requests

client = UserApiClient("http://127.0.0.1:8000")

print("✅ Health check:", client.health_check())

new_user = {
    "id": "309277852",
    "name": "Test User2",
    "phone": "+072545654567",
    "address": "Rosh Ha Ayin"
}

try:
    print("🚀 Creating user...")
    created = client.create_user(new_user)
    print("✅ Created:", created)
except ValueError as ve:
    print("⚠️ Client-side validation error:", ve)
except requests.exceptions.HTTPError as http_err:
    try:
        error_details = http_err.response.json()
        print("❌ HTTP error occurred:", error_details)
    except Exception:
        print("❌ HTTP error occurred (no JSON):", str(http_err))

print("📦 All users:", client.list_users())

try:
    user = client.get_user("123456789")
    print("🔍 Fetched:", user)
except ValueError as ve:
    print("❌", ve)
except requests.exceptions.HTTPError as http_err:
    print("❌ HTTP error during get_user:", http_err)
