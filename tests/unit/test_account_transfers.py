from src.account import Account

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