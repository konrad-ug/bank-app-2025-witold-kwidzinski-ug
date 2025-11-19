from src.account import Account

class CompanyAccount(Account):
    def __init__(self, company_name, nip):
        super().__init__()
        self.company_name = company_name
        self.nip = nip if self.is_nip_valid(nip) else "Invalid"
        self.balance = 0.0
        self.express_fee = 5.0


    def take_loan(self, amount):
        if amount > 0 and self.balance >= amount * 2 and -1775 in self.history:
            self.balance += amount
            return True
        return False

    def is_nip_valid(self, nip):
        if nip is not None and len(nip) == 10:
            return True
        return False