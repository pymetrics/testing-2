# accounts/models/mixins.py

class SlackAuthMixin:
    """Overrides user-y things we don't need"""
    def check_password(self, raw_password):
        return True
