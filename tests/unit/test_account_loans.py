from src.personal_account import PersonalAccount
import pytest

class TestAccountLoans:

    @pytest.fixture
    def account(self):
        account = PersonalAccount("John", "Doe", "12345678909")
        return account

    def test_loan_good_incoming_transfer_amount(self, account):
        account.history = [50.0, 80.0, 130.0]

        assert account.submit_for_loan(50.0) == True

    def test_loan_low_incoming_transfer_amount(self, account):
        account.history = [50.0, 80.0]

        assert account.submit_for_loan(50.0) == False

    def test_loan_wrong_incoming_transfer_amount(self, account):
        account.history = [50.0, 80.0, -30.0, 20.0]

        assert account.submit_for_loan(50.0) == False

    def test_loan_good_overall_transfer_amount(self, account):
        account.history = [50.0, 80.0, -30.0, 20.0, -40.0]

        assert account.submit_for_loan(60.0) == True

    def test_loan_low_overall_transfer_amount(self, account):
        account.history = [50.0, 80.0, -30.0, 20.0, -40.0]

        assert account.submit_for_loan(100.0) == False