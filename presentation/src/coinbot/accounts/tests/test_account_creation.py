# accounts/tests/test_account_creation.py
from django.test import TestCase
from django.contrib.auth import get_user_model
from accounts.models import CoinAccount

class CoinAccountCreationTests(TestCase):
    def test_account_defaults(self):
        """Account defaults to zero balance"""
        User = get_user_model()
        test_user = User.objects.create(user_id=1, team_id=1)
        account = CoinAccount.objects.create(user=test_user)
        self.assertEqual(account.balance, 0.0)
