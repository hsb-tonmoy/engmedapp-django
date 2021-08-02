from accounts.views import (
    BlacklistTokenUpdateView,
    ProfileView
)
from django.urls import path, re_path

app_name = 'accounts'

urlpatterns = [
    path('logout/', BlacklistTokenUpdateView.as_view(),
         name='logout'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile')

]
