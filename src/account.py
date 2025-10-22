class Account:
    def __init__(self, first_name, last_name, pesel, promo_code=None):
        self.first_name = first_name
        self.last_name = last_name
        self.pesel = pesel if self.is_pesel_valid(pesel) else "Invalid"
        self.balance = 50.0 if self.is_promo_valid(promo_code) and self.can_pesel_promo(pesel) else 0.0

    def is_pesel_valid(self, pesel):
        if pesel and len(pesel) == 11:
            return True
        return False

    def is_promo_valid(self, promo_code):
        if promo_code and len(promo_code) == 8 and promo_code[0:5] == "PROM_":
            return True
        return False

    def can_pesel_promo(self, pesel):
        if int(pesel[0:2]) > 60:
            return True
        return False