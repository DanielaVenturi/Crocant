from rest_framework.viewsets import ModelViewSet

from core.models import Cidade
from core.serializers import CidadeSerializer


class CidadeViewSet(ModelViewSet):
    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer