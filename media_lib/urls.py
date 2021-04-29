from media_lib.views import ImageView, SingleImageView
from django.urls import path

app_name = 'media_lib'

urlpatterns = [
    path('images/<int:pk>/', SingleImageView.as_view(), name='image'),
    path('images/', ImageView.as_view(), name='images'),
]
