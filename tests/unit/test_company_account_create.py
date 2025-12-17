import pytest
from src.company_account import CompanyAccount
from pytest_mock import mocker

class TestCompanyAccount:
    def test_account_creation(self, mocker):
        mock = mocker.patch('src.company_account.requests.get')

        mock.return_value.status_code = 200
        mock.return_value.json.return_value = {"result": {"subject": {"statusVat": "Czynny"}}}

        account = CompanyAccount("company","1234567890")
        assert account.company_name == "company"
        assert account.nip == "1234567890"

    def test_nip_empty(self):
        account = CompanyAccount("company", "")
        assert account.nip == "Invalid"

    # def test_nip_too_short(self):
    #     account = CompanyAccount("company", "1234")
    #     assert account.nip == "Invalid"

    # def test_nip_too_long(self):
    #     account = CompanyAccount("company", "12345678909876")
    #     assert account.nip == "Invalid"

    def test_nip_none(self):
        account = CompanyAccount("company", None)
        assert account.nip == "Invalid"

    def test_invalid_nip(self, mocker):
        mock = mocker.patch('src.company_account.requests.get')

        mock.return_value.status_code = 200
        mock.return_value.json.return_value = {"result": {"message":"Nieprawidłowy NIP."}}

        with pytest.raises(ValueError, match="Company not registered!!"):
            account = CompanyAccount("company", "1234567890")



