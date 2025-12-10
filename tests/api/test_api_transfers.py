import pytest
import requests

class TestAPITransfers:

    def setup_method(self):
        mainurl = "http://localhost:5000/api/accounts"

        requests.delete(f"{mainurl}/89009290982")
        requests.delete(f"{mainurl}/12345678909")

        requests.post(mainurl, json={
            "first_name": "james",
            "last_name": "hetfield",
            "pesel": "89009290982",
            "balance": 50
        })
        requests.post(mainurl, json={
            "first_name": "john",
            "last_name": "doe",
            "pesel": "12345678909",
            "balance": 0
        })


    def test_account_transfer_pesel_not_found(self):
        url = "http://localhost:5000/api/accounts/12121212121/transfer"

        request = requests.post(url, json={"amount": 25, "type": "outgoing"})
        assert request.status_code == 404
        assert request.json() == "Account not found."

    def test_wrong_transfer_type(self):
        url = "http://localhost:5000/api/accounts/89009290982/transfer"

        request = requests.post(url, json={"amount": 25, "type": "lalaalala"})
        assert request.status_code == 406

    def test_insufficient_transfer(self):
        url = "http://localhost:5000/api/accounts/89009290982/transfer"

        request = requests.post(url, json={"amount": 75, "type": "outgoing"})
        assert request.status_code == 422


    def test_account_incoming_transfer(self):
        url = "http://localhost:5000/api/accounts/89009290982/transfer"

        request = requests.post(url, json={"amount": 25, "type": "incoming"})
        assert request.status_code == 200
        assert request.json() == "Zlecenie przyjęto do realizacji."

        request = requests.get("http://localhost:5000/api/accounts/89009290982")
        assert request.json()["balance"] == 75

    def test_account_outgoing_transfer(self):
        url = "http://localhost:5000/api/accounts/89009290982/transfer"

        request = requests.post(url, json={"amount": 25, "type": "outgoing"})
        assert request.status_code == 200
        assert request.json() == "Zlecenie przyjęto do realizacji."

        request = requests.get("http://localhost:5000/api/accounts/89009290982")
        assert request.json()["balance"] == 25

    def test_account_express_transfer(self):
        url = "http://localhost:5000/api/accounts/89009290982/transfer"

        request = requests.post(url, json={"amount": 25, "type": "express"})
        assert request.status_code == 200
        assert request.json() == "Zlecenie przyjęto do realizacji."

        request = requests.get("http://localhost:5000/api/accounts/89009290982")
        assert request.json()["balance"] == 24