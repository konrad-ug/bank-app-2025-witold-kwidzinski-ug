import pytest
import requests

class TestApiCrud:

    @pytest.fixture(scope="function", autouse=True)
    def account_data(self):
        account_data = {
            "first_name": "james",
            "last_name": "hetfield",
            "pesel": "89009290982",
            "balance": 0
        }
        return account_data

    def test_create_account(self, account_data):
        url = "http://localhost:5000/api/accounts"

        response = requests.post(url, json=account_data)
        assert response.status_code == 201
        assert response.json()["message"] == "Account created"

    def test_create_account_same_pesel(self, account_data):

        url = "http://localhost:5000/api/accounts"

        response = requests.post(url, json=account_data)
        assert response.status_code == 409
        assert response.json() == "Account with this pesel already exists."

    def test_count(self):
        url = "http://localhost:5000/api/accounts/count"
        response = requests.get(url)
        assert response.status_code == 200
        assert response.json()["count"] == 1

    def test_get_account_by_pesel(self, account_data):
        url = f"http://localhost:5000/api/accounts/{account_data['pesel']}"
        response = requests.get(url)
        assert response.status_code == 200
        assert response.json() == account_data

    def test_get_account_by_pesel_bad(self, account_data):
        url = f"http://localhost:5000/api/accounts/02938576859"
        response = requests.get(url)
        assert response.status_code == 404
        assert response.json() == "No account found."

    def test_update_account(self, account_data):
        url = f"http://localhost:5000/api/accounts/{account_data['pesel']}"
        response = requests.patch(url, json={"last_name": "bond"})
        assert response.status_code == 200
        res2 = requests.get(url)
        assert res2.json() == {"first_name": "james", "last_name": "bond", "pesel": "89009290982", "balance": 0}

    def test_update_pesel_fail(self, account_data):
        url = f"http://localhost:5000/api/accounts/{account_data['pesel']}"
        response = requests.patch(url, json={"pesel": "67340652104"})
        assert response.status_code == 405

    def test_delete_account(self, account_data):
        url = f"http://localhost:5000/api/accounts/{account_data['pesel']}"
        response = requests.delete(url)
        assert response.status_code == 200
        res2 = requests.get(url)
        assert res2.json() == "No account found."