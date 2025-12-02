import pytest
from src.account_registry import AccountRegistry
from src.personal_account import PersonalAccount

class TestAccountRegistry:

    @pytest.fixture
    def account_registry(self):
        registry = AccountRegistry()
        registry.add_account(PersonalAccount("John", "Doe", "12345678909"))
        registry.add_account(PersonalAccount("Doe", "John", "09876543212"))
        return registry

    def test_get_account_by_pesel_found(self, account_registry):
        assert account_registry.get_account_by_pesel("12345678909").__dict__ == PersonalAccount("John", "Doe", "12345678909").__dict__

    def test_get_account_by_pesel_notfound(self, account_registry):
        assert account_registry.get_account_by_pesel("12345654321") is None

    def test_get_all_accounts(self, account_registry):
        assert [acc.__dict__ for acc in account_registry.get_all_accounts()] == [PersonalAccount("John", "Doe", "12345678909").__dict__, PersonalAccount("Doe", "John", "09876543212").__dict__]

    def test_get_account_count(self, account_registry):
        assert account_registry.get_account_count() == 2



