# accounts/models/account.py
from django.db import models
from django.conf import settings
from coinbase import get_price


class CoinAccount(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name='accounts')
    coin = models.CharField(max_length=3, default="BTC")
    balance = models.FloatField(default=0)

    def get_balance_in_fiat(self, fiat='USD'):
        current_price = get_price(self.coin, fiat)
        return self.balance * current_price
