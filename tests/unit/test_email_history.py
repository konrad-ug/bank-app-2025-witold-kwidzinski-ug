from pytest_mock import mocker
from src.personal_account import PersonalAccount
from datetime import datetime
# from src.personal_account import PersonalAccount
# from src.company_account import CompanyAccount

class TestEmailHistory:
    today = datetime.today().strftime("%Y-%m-%d")
    email = "super@mail.com"
    def test_personal_account_email(self, mocker):
        account = PersonalAccount("John", "Doe", "12345678909")
        account.history = [3, 14, -8, 12]

        mock = mocker.patch("src.account.SMTPClient.send", return_value=True)
        result = account.send_history_via_email(self.email)

        assert result == True
        mock.assert_called_once()
        subject = mock.call_args[0][0]
        text = mock.call_args[0][1]
        email_adress = mock.call_args[0][2]
        assert subject == f"Account Transfer History {self.today}"
        assert email_adress == self.email
        assert text == f"Personal account history: {account.history}"

    def test_personal_account_email_failed(self, mocker):
        account = PersonalAccount("John", "Doe", "12345678909")
        account.history = [3, 14, -8, 12]

        mock = mocker.patch("src.account.SMTPClient.send", return_value=False)
        result = account.send_history_via_email(self.email)

        assert result == False