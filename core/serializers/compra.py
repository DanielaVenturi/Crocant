from rest_framework.serializers import CharField, ModelSerializer, SerializerMethodField
from core.models import Compra, ItensCompra

class ItensCompraSerializer(ModelSerializer):
    total = SerializerMethodField()  # Campo para calcular o total

    def get_total(self, instance):
        return instance.pedido.preco * instance.quantidade  # Certifique-se de que 'pedido.preco' existe no modelo

    class Meta:
        model = ItensCompra
        fields = ("pedido", "quantidade", "total")  # Adiciona 'total' ao fields
        depth = 1


class CompraSerializer(ModelSerializer):
    usuario = CharField(source="usuario.email", read_only=True)
    itens = ItensCompraSerializer(many=True, read_only=True)

    class Meta:
        model = Compra
        fields = "__all__"
