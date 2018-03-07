# Generated by Django 2.0.2 on 2018-02-13 19:19

import accounts.models.mixins
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SlackUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('user_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('team_id', models.CharField(max_length=50)),
                ('display_name', models.CharField(max_length=100)),
            ],
            bases=(accounts.models.mixins.SlackAuthMixin, models.Model),
        ),
        migrations.CreateModel(
            name='CoinAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coin', models.CharField(default='BTC', max_length=3)),
                ('balance', models.FloatField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='slackuser',
            unique_together={('user_id', 'team_id')},
        ),
    ]