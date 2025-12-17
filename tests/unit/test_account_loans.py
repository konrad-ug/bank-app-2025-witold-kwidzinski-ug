from src.personal_account import PersonalAccount
from src.company_account import CompanyAccount
import pytest
from pytest_mock import mocker

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



    @pytest.mark.parametrize("balance,loan,history,expected",
                             [(100, -48, [3, 18, 25, -14, -1775], False),
                              (84, 50, [3, 18, 25, -14, -1775], False),
                              (100, 48, [3, 18, 25, -14], False),
                              (100, 48, [3, 18, 25, -14, -1775], True)],
                             ids= [
                                 "negative loan",
                                 "loan amount too big",
                                 "no zus payment",
                                 "everything correct"
                             ])

    def test_company_loan(self, balance, loan, history, expected, mocker):
        mock = mocker.patch('src.company_account.requests.get')

        mock.return_value.status_code = 200
        mock.return_value.json.return_value = {"result": {"subject": {"statusVat": "Czynny"}}}
        company_account = CompanyAccount("company", "1234567890")
        company_account.balance = balance
        company_account.history = history

        assert company_account.take_loan(loan) == expected