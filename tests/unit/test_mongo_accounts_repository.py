import pytest
from pytest_mock import mocker
from src.mongo_accounts_repository import MongoAccountsRepository
from src.personal_account import PersonalAccount
from src.account_registry import AccountRegistry

class TestMongoAccountsRepository:

    def test_save_all(self, mocker):
        mock_collection = mocker.Mock()
        repo = MongoAccountsRepository(collection=mock_collection)


        acc1 = PersonalAccount("John", "Doe", "12345678909")

        acc2 = PersonalAccount("Dohn", "Joe", "90987654321")

        repo.save_all([acc1, acc2])

        mock_collection.delete_many.assert_called_once_with({})
        assert mock_collection.update_one.call_count == 2

    def test_load_all(self, mocker):
        mock_collection = mocker.Mock()
        repo = MongoAccountsRepository(collection=mock_collection)

        mock_collection.find.return_value = [
            {"pesel": "12345678909"},
            {"pesel": "90987654321"}
        ]

        registry = AccountRegistry()
        registry.add_account = mocker.Mock()

        repo.load_all(registry)

        assert registry.accounts == []
        assert registry.add_account.call_count == 2