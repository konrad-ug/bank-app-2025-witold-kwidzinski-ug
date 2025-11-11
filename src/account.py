class Account:
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
