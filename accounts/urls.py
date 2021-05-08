from accounts.views import CookieTokenRefreshView, CookieTokenObtainPairView, BlacklistTokenUpdateView, ProfileView
from django.urls import path

app_name = 'accounts'

urlpatterns = [
    path('auth/token/', CookieTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('auth/token/refresh/',
         CookieTokenRefreshView.as_view(), name='token_refresh'),
    path('logout/blacklist/', BlacklistTokenUpdateView.as_view(),
         name='blacklist'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile')

]
