from django.db import models
from .produto import Produto

class Pedido(models.Model):  
    data = models.DateField(auto_now_add=True)
    produto = models.ManyToManyField(Produto, related_name="pedidos", blank=True)

    def __str__(self):
        return f"({self.id}) {self.data} -- Total: R$ {self.get_total_value():.2f}"

    def get_total_value(self):
        return sum(produto.preco for produto in self.produto.all())

    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"