from mock import patch
from django.test import TestCase
from django.urls import reverse
from accounts.models import SlackUser, CoinAccount

class SlashCommandPostTest(TestCase):
    @patch('accounts.models.account.get_price', return_value=1000)
    def test_get_command(self, _):
        user = SlackUser.objects.create(user_id=1, team_id=1)
        account = CoinAccount.objects.create(user=user, coin='ETH', balance=2)
        url = reverse('slash_command_post')
        post_data = {'user_id': 1, 'team_id': 1,
                     'text': 'get my ETH balance'}
        resp = self.client.post(url, post_data)
        self.assertEqual(resp.content, b"Your ETH balance is $2000.0")
