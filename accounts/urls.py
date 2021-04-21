from accounts.views import BlacklistTokenUpdateView
from django.urls import path

app_name = 'accounts'

urlpatterns = [
    path('logout/blacklist/', BlacklistTokenUpdateView.as_view(),
         name='blacklist')
    # path('token/', CustomTokenObtainPairView.as_view(),
    #      name='jwt-token')

]
