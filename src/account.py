from lib.smtp import SMTPClient
from datetime import datetime

class Account:
    history_email_template = "Account"
    def __init__(self):
        self.balance = 0.0
        self.express_fee = 0.0
        self.history = []

    def incoming_transfer(self,amount):
        if amount > 0:
            self.balance += amount
            self.history.append(amount)

    def outgoing_transfer(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.history.append(amount * -1)

    def express_transfer(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount + self.express_fee
            self.history.append(amount * -1)
            self.history.append(self.express_fee * -1)

    def send_history_via_email(self, email_adress):
        today = datetime.today().strftime("%Y-%m-%d")
        return SMTPClient.send(f"Account Transfer History {today}",
                        f"{self.history_email_template} account history: {self.history}",
                        email_adress)