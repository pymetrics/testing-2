from django.test import TestCase
from django.contrib.auth import models

from coinbot.models import CoinAccount

class AnnoyingTest(TestCase):
    def test_one(self):
        # Manually create a user with the ORM
        user = User.objects.create(first_name='Alice', last_name='Testuser',
                                   email='alice@example.com')
        account = CoinAccount.objects.create(user=user)
        # test somethign
