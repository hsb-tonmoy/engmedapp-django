from accounts.views import (
    AccountView,
    BlacklistTokenUpdateView,
    ProfileView
)

from django.urls import path, include
from rest_framework.routers import DefaultRouter

app_name = 'accounts'

router = DefaultRouter()
router.register(r'profile', ProfileView)

urlpatterns = [
    path('logout/', BlacklistTokenUpdateView.as_view(),
         name='logout'),
    path('account/<str:pk>/', AccountView.as_view(), name='account'),
    path('', include(router.urls)),

]
