from datetime import datetime

from django.contrib.auth import get_user_model
from django.shortcuts import render

from webapp.forms import RegistrationForm


User = get_user_model()


def main_view(request):
    year = datetime.now().year
    return render(request, 'web/main.html', {
        'year': year
    })


def registration_view(request):
    form = RegistrationForm()
    is_success = False
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = User(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email']
            )
            user.set_password(form.cleaned_data['password'])
            user.save()
            print(form.cleaned_data)
    return render(request, 'web/registration.html', {
        'form': form, 'is_success': is_success
    })
