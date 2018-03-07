from django.test import SimpleTestCase
from mock import patch
from accounts.models import CoinAccount

class CoinAccountMethodTests(SimpleTestCase):
    @patch('accounts.models.account.get_price', return_value=10000.0)
    def test_get_balance_in_fiat(self, mock_get_price):
        account = CoinAccount(balance=2, coin='BTC')

        result = account.get_balance_in_fiat()

        expected = 20000.0
        self.assertEqual(result, expected)
