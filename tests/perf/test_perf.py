import unittest
import pytest
import requests

class PerfApiTest(unittest.TestCase):
    body = {
        "first_name": "John",
        "last_name": "Doe",
        "pesel": "12345678909"
    }
    url = "http://localhost:5000/api/accounts"

    def test_create_delete_perf_test(self):
        for _ in range(100):
            create_response = requests.post(self.url, json=self.body, timeout=0.5)
            assert create_response.status_code == 201
            delete_response = requests.delete(f"{self.url}/{self.body['pesel']}", timeout=0.5)
            assert delete_response.status_code == 200

    def test_create_transfer_perf_test(self):
        create_response = requests.post(self.url, json=self.body, timeout=0.5)
        assert create_response.status_code == 201
        for _ in range(100):
            incoming_transfer_response = requests.post(f"{self.url}/{self.body['pesel']}/transfer", json={"type": "incoming", "amount": 100}, timeout=0.5)
            assert incoming_transfer_response.status_code == 200
        get_balance = requests.get(f"{self.url}/{self.body['pesel']}", timeout=0.5)
        assert get_balance.status_code == 200
        print(get_balance.json()["balance"])