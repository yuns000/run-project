from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('account_creation/', views.account_creation, name='account_creation'),
]