class Account:
    def __init__(self):
        self.balance = 0.0
        self.express_fee = 0.0

    def incoming_transfer(self,amount):
        if amount > 0:
            self.balance += amount

    def outgoing_transfer(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount

    def express_transfer(self, amount):
        if amount > 0 and amount <= self.balance:
            self.outgoing_transfer(amount)
            self.balance -= self.express_fee
