from accounts.views import (
    CookieTokenRefreshView,
    CookieTokenObtainPairView,
    SocialJWTPairOnlyAuthView,
    AuthorizationURL,
    BlacklistTokenUpdateView,
    ProfileView
)
from django.urls import path, re_path

app_name = 'accounts'

urlpatterns = [
    re_path(
        r"^o/(?P<provider>\S+)/$",
        AuthorizationURL.as_view(),
        name="auth-url",
    ),
    re_path(r'^social/(?:(?P<provider>[a-zA-Z0-9_-]+)/?)?$',
            SocialJWTPairOnlyAuthView.as_view(),
            name='login_social_jwt_pair'),
    path('login/', CookieTokenObtainPairView.as_view(),
         name='login'),
    path('login/refresh/',
         CookieTokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', BlacklistTokenUpdateView.as_view(),
         name='logout'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile')

]
