from accounts.views import BlacklistTokenUpdateView, CustomTokenObtainPairView
from django.urls import path

app_name = 'accounts'

urlpatterns = [
    path('logout/blacklist/', BlacklistTokenUpdateView.as_view(),
         name='blacklist')
]
