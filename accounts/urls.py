from django.urls import path
from .views import AccountRegistration, BlacklistTokenUpdateView

app_name = 'accounts'

urlpatterns = [
    path('register/', AccountRegistration.as_view(), name="registration"),
    path('logout/blacklist/', BlacklistTokenUpdateView.as_view(), name="blacklist"),
]
