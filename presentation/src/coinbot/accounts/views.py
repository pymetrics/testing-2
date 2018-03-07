# accounts/views.py
from django.http import HttpResponse
from .forms import SlashCommandForm

def handle_command(request):
    if request.method == 'POST':
        form = SlashCommandForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            response = user.apply_command(**form.tokens)
            return HttpResponse(response)
        else:
            print(form.errors)
            return HttpResponse(status=400, content=str(form.errors))
    return HttpResponse(status=405)
