from django.urls import path
from .views import create_api_key

urlpatterns = [
    path('api/generate-key/', create_api_key, name='create-api-key'),
]
