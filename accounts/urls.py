from accounts.views import BlacklistTokenUpdateView, ProfileView
from django.urls import path

app_name = 'accounts'

urlpatterns = [
    path('logout/blacklist/', BlacklistTokenUpdateView.as_view(),
         name='blacklist'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile')

]
