import pytest
import requests


from pymongo import MongoClient

class TestApiSaveLoad:

    def setup_method(self):
        self.link = "http://localhost:5000/api/accounts"

        client = MongoClient()
        self.collection = client["bank_app"]["accounts"]
        self.collection.delete_many({})

        requests.post(f"{self.link}", json={
            "first_name": "John",
            "last_name": "Doe",
            "pesel": "12345678909",
            "balance": 0
        })

        requests.post(f"{self.link}", json={
            "first_name": "Abraham",
            "last_name": "Lincoln",
            "pesel": "38495162940",
            "balance": 0
        })



    def test_save_registry(self):
        r = requests.post(f"{self.link}/save")

        assert r.status_code == 200

        dbaccounts = list(self.collection.find())
        assert len(dbaccounts) == 2

        pesels = {d["pesel"] for d in dbaccounts}
        assert pesels == {"12345678909", "38495162940"}

    def test_load_registry(self):
        requests.post(f"{self.link}/save")

        requests.post(f"{self.link}", json={
            "first_name": "Joe",
            "last_name": "Biden",
            "pesel": "01010101010",
            "balance": 0
        })

        r = requests.post(f"{self.link}/load")

        assert r.status_code == 200

        getaccs = requests.get(self.link)

        assert getaccs.status_code == 200

        pesels = {d["pesel"] for d in getaccs.json()}
        assert pesels == {"12345678909", "38495162940"}