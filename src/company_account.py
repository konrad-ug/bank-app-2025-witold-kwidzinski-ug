import os
from datetime import datetime
from src.account import Account
import requests

class CompanyAccount(Account):
    BANK_APP_MF_URL = os.getenv("BANK_APP_MF_URL", "https://wl-test.mf.gov.pl/")
    def __init__(self, company_name, nip):
        super().__init__()
        self.company_name = company_name
        self.balance = 0.0
        self.express_fee = 5.0



        if nip is None or len(nip) == 0:
            self.nip = "Invalid"
            return
        if len(nip) == 10:
            if not self.is_nip_valid(nip):
                raise ValueError("Company not registered!!")
            self.nip = nip



    def take_loan(self, amount):
        if amount > 0 and self.balance >= amount * 2 and -1775 in self.history:
            self.balance += amount
            return True
        return False

    def is_nip_valid(self, nip):
        today = datetime.today().strftime("%Y-%m-%d")
        request = requests.get(f"{self.BANK_APP_MF_URL}/api/search/nip/{nip}?date={today}")


        print(request.json())
        data = request.json().get("result", {}).get("subject")

        if not data:
            return False

        return data.get("statusVat") == "Czynny"
