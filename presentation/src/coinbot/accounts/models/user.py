# accounts/models/user.py
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser

from .mixins import SlackAuthMixin
from .managers import SlackUserManager

class SlackUser(SlackAuthMixin, AbstractBaseUser):
    USERNAME_FIELD = 'user_id'
    user_id = models.CharField(max_length=50, primary_key=True)
    team_id = models.CharField(max_length=50)
    display_name = models.CharField(max_length=100)
    objects = SlackUserManager
    class Meta:
        unique_together = ('user_id', 'team_id')

    def apply_command(self, **tokens):
        cmd = tokens['command']
        if cmd == 'get':
            return self.get_balance(tokens['coin'])
        if cmd == 'set':
            return self.set_balance(tokens['coin'], tokens['amount'])
        return "I'm sorry, I didn't understand that request"

    def get_balance(self, coin):
        account = self.accounts.filter(coin=coin).first()
        balance = account.get_balance_in_fiat() if account else 0
        return f"Your {coin} balance is ${balance}"

    def set_balance(self, coin, amount):
        account, created = self.accouns.get_or_create(coin=coin,
            defaults={'user_id': self.id, 'balance': 0.0})
        if created:
            return f"Created {coin} account with balance {balance}"
        return f"Set your {coin} account balance to {balance}"
