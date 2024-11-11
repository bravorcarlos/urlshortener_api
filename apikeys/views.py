from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import AllowAny
from rest_framework_api_key.models import APIKey

# Create your views here.
@swagger_auto_schema(method='post', auto_schema=None)
@api_view(['POST'])
@permission_classes([AllowAny])
def create_api_key(request):
    name = request.data.get('name')
    if not name:
        return Response({"error": "El campo 'name' es requerido."}, status=status.HTTP_400_BAD_REQUEST)

    api_key, key = APIKey.objects.create_key(name=name)
    return Response({"name": name, "api_key": key}, status=status.HTTP_201_CREATED)