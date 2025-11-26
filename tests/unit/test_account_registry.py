import pytest
from src.account_registry import AccountRegistry
from src.personal_account import PersonalAccount

class TestAccountRegistry:

    @pytest.fixture
    def account_registry(self):
        return AccountRegistry()



