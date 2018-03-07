import factory
from accounts.models import SlackUser, CoinAccount

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = SlackUser
    user_id = factory.Sequence(lambda n: n + 1000)
    team_id = factory.Faker('numerify', text='T#######')
    display_name = factory.Faker('user_name')


class CoinAccountFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CoinAccount
    user = factory.SubFactory(UserFactory)
    coin = 'BTC'
    balance = 0
