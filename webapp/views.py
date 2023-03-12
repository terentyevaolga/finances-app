from datetime import datetime

from django.contrib.auth import get_user_model, authenticate, login
from django.shortcuts import render, redirect

from webapp.forms import RegistrationForm, AuthForm

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


def auth_view(request):
    form = AuthForm()
    if request.method == 'POST':
        form = AuthForm(data=request.POST)
        if form.is_valid():
            user = authenticate(**form.cleaned_data)
            if user is None:
                form.add_error(None, 'Введены неверные данные! Повторите попытку')
            else:
               login(request, user)
               return redirect('main')
    return render(request, 'web/auth.html', {'form': form})



