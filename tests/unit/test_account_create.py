from src.personal_account import PersonalAccount


class TestPersonalAccount:
    def test_PersonalAccount_creation(self):
        account = PersonalAccount("John", "Doe", "12345678909")
        assert account.first_name == "John"
        assert account.last_name == "Doe"
        assert account.balance == 0.0
        assert account.pesel == "12345678909"

    def test_pesel_too_long(self):
        account = PersonalAccount("Joe", "Dohn", "1234567890987")
        assert account.pesel == "Invalid"

    def test_pesel_too_short(self):
        account = PersonalAccount("Joe", "Dohn", "1234587")
        assert account.pesel == "Invalid"

    def test_pesel_empty(self):
        account = PersonalAccount("Joe", "Dohn", "")
        assert account.pesel == "Invalid"

    def test_promo_good(self):
        account = PersonalAccount("John", "Doe", "92345678909", "PROM_123")
        assert account.balance == 50.0

    def test_promo_length(self):
        account = PersonalAccount("John", "Doe", "92345678909", "PROM_12453")
        assert account.balance == 0.0

    def test_promo_correct_prefix(self):
        account = PersonalAccount("John", "Doe", "92345678909", "PORM_153")
        assert account.balance == 0.0

    def test_correct_age(self):
        account = PersonalAccount("John", "Doe", "95345678909", "PROM_153")
        assert account.balance == 50.0

    def test_wrong_age(self):
        account = PersonalAccount("John", "Doe", "12345678909", "PROM_153")
        assert account.balance == 0.0


