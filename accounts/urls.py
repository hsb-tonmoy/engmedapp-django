from django.urls import path
from .views import AccountRegistration

app_name = 'accounts'

urlpatterns = [
    path('register/', AccountRegistration.as_view(), name="registration")
]
