import re
from django import forms
from .models.user import SlackUser

set_rgx = re.compile(r'^(?P<command>set)\s+.*(?P<coin>[A-Z]{3}).*(?P<amount>\d+\.+\d+)')
get_rgx = re.compile(r'^(?P<command>get)\s+.*(?P<coin>[A-Z]{3}).*')

class SlashCommandForm(forms.Form):
    # token = forms.CharField()
    team_id = forms.CharField()
    user_id = forms.CharField()
    # response_url = forms.URLField()
    # command = forms.CharField()
    text = forms.CharField()

    def clean_text(self):
        value = self.cleaned_data['text']
        """Text is a valid command"""
        for rgx in (set_rgx, get_rgx):
            match = rgx.search(value)
            if match:
                self.tokens = match.groupdict()
                return
        raise forms.ValidationError(f'"{value}" is not a valid command"')

    def get_user(self):
        assert self.cleaned_data
        return SlackUser.objects.get(team_id=self.cleaned_data['team_id'],
                                     user_id=self.cleaned_data['user_id'])
