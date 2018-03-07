import requests_mock
from django.test import SimpleTestCase
from .factories import CoinAccountFactory

class CoinAccountGetBalanceTests(SimpleTestCase):
    @requests_mock.Mocker()
    def test_get_balance_with_request_mock(self, m):
        account = CoinAccountFactory.build(balance=1)
        # get_balance will GET this URL:
        url = f'https://api.coinbase.com/v2/prices/{account.coin}-USD/spot'
        # This is the response we want:
        response = {"data": {"amount": "1015.00",
                             "currency": "USD"}}
        m.register_uri('GET', url, json=response)

        balance = account.get_balance_in_fiat()

        self.assertEqual(balance, 1015.00)
