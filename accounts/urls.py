from accounts.views import CookieTokenRefreshView, CookieTokenObtainPairView, BlacklistTokenUpdateView, ProfileView
from django.urls import path

app_name = 'accounts'

urlpatterns = [
    path('login/', CookieTokenObtainPairView.as_view(),
         name='login'),
    path('login/refresh/',
         CookieTokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', BlacklistTokenUpdateView.as_view(),
         name='logout'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile')

]
