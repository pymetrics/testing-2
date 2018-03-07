# accounts/models/managers.py
from django.contrib.auth.models import BaseUserManager

class SlackUserManager(BaseUserManager):
    def create_user(self, user_id, team_id, display_name):
        pass
