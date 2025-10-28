from src.account import Account
from src.personal_account import PersonalAccount
from src.company_account import CompanyAccount

class TestAccountTransfers:
    def test_incoming_transfer(self):
        account = Account() #1. set up
        account.incoming_transfer(25.0) #2. action
        assert account.balance == 25.0 #3. assertion
    def test_outgoing_transfer_sufficient_balance(self):
        account = Account()
        account.balance = 100
        account.outgoing_transfer(50.0)
        assert account.balance == 50.0
    def test_outgoing_transfer_insufficient_balance(self):
        account = Account()
        account.incoming_transfer(25.0)
        account.outgoing_transfer(50.0)
        assert account.balance == 25.0
    def test_outgoing_transfer_negative(self):
        account = Account()
        account.incoming_transfer(25.0)
        account.outgoing_transfer(-50.0)
        assert account.balance == 25.0
    def test_express_transfer(self):
        account = PersonalAccount("John", "Doe", "12345678909")
        account2 = CompanyAccount("company", "1234567890")

        account.incoming_transfer(50.0)
        account2.incoming_transfer(50.0)

        account.express_transfer(25.0)
        account2.express_transfer(25.0)

        assert account.balance == 24.0
        assert account2.balance == 20.0
    def test_zero_express_transfer(self):
        account = PersonalAccount("John", "Doe", "12345678909")
        account.express_transfer(50.0)
        assert account.balance == 0.0

