from src.company_account import CompanyAccount

class TestCompanyAccount:
    def test_account_creation(self):
        account = CompanyAccount("company","1234567890")
        assert account.company_name == "company"
        assert account.nip == "1234567890"

    def test_nip_empty(self):
        account = CompanyAccount("company", "")
        assert account.nip == "Invalid"

    def test_nip_too_short(self):
        account = CompanyAccount("company", "1234")
        assert account.nip == "Invalid"

    def test_nip_too_long(self):
        account = CompanyAccount("company", "12345678909876")
        assert account.nip == "Invalid"

    def test_nip_empty(self):
        account = CompanyAccount("company", None)
        assert account.nip == "Invalid"