from rest_framework.serializers import ModelSerializer

from core.models import Pedido


class PedidoSerializer(ModelSerializer):
    class Meta:
        model = Pedido
        fields = "__all__"
        depth = 2

class PedidoWriteSerializer(ModelSerializer):
    class Meta:
        model = Pedido
        fields = ["produto", "data"]