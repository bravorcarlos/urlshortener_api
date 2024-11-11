from django.urls import path
from .views import CreateLinkAPIView, LinkDetailAPIView

urlpatterns = [
    path('api/link/', CreateLinkAPIView.as_view(), name='create-link'),
    path('api/link/<str:code>/', LinkDetailAPIView.as_view(), name='get-link'),
]
