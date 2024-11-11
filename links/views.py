from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework_api_key.permissions import HasAPIKey
from .models import Link
from .serializers import LinkSerializer
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from hashids import Hashids

class CreateLinkAPIView(APIView):
    permission_classes = [HasAPIKey]

    @swagger_auto_schema(
        request_body=LinkSerializer,
        # request_body=openapi.Schema(
        #     type=openapi.TYPE_OBJECT,
        #     properties={
        #         'url': openapi.Schema(type=openapi.TYPE_STRING, description='URL to be shortened'),
        #     },
        #     required=['url'],
        #     example={
        #         'url': 'https://example.com'
        #     }
        # ),
        responses={
            201: openapi.Response('Link creado', LinkSerializer),
            400: 'Entrada inválida'
        }
    )
    def post(self, request):
        serializer = LinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LinkDetailAPIView(RetrieveAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    lookup_field = 'code'
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        code = kwargs.get('code')
        try:
            link_id = Hashids(min_length=8).decode(code)[0]
            link = Link.objects.get(id=link_id)
            link.click_count += 1
            link.save()
            serializer = self.get_serializer(link)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except (IndexError, Link.DoesNotExist):
            return Response({"error": "Este enlace no existe"}, status=status.HTTP_404_NOT_FOUND)