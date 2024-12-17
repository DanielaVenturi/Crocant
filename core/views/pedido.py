from rest_framework.viewsets import ModelViewSet

from core.models import Pedido
from core.serializers import PedidoSerializer, PedidoWriteSerializer
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response



class PedidoViewSet(ModelViewSet):
    queryset = Pedido.objects.all()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return PedidoSerializer
        else:
            return PedidoWriteSerializer
    
    @action(
        detail=False,
        methods=["get"],
        url_path="pedido-atual",
    )
    def buscar_ultimo_pedido(self, request, pk=None, *args, **kwargs):
        try:
            pedido = Pedido.objects.last()
            if not pedido:
                return Response(
                    {"detail": "Nenhum pedido encontrado."},
                    status=status.HTTP_404_NOT_FOUND,
                )

            serializer = PedidoSerializer(pedido)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                {"detail": f"Erro interno: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

class UltimoPedidoViewSet(ModelViewSet):
    queryset = [Pedido.objects.last()]
    serializer_class = PedidoSerializer