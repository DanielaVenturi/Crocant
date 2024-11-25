from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from core.models import Categoria
from core.serializers import CategoriaSerializer



class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

# class CategoriaListView(APIView):
#     def get(self, request):
#         categorias = Categoria.objects.all()
#         serializer = CategoriaSerializer(categorias, many=True)
#         return Response(serializer.data)