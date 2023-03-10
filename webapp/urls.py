from django.urls import path

from webapp.views import main_view, registration_view

urlpatterns = [
    path('', main_view),
    path('registration', registration_view),
]

