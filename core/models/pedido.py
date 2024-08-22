from django.db import models
from django.utils import timezone 
from .categoria import Categoria


class Pedido(models.Model):  
    data = models.DateField(auto_now_add=True)
    categoria = models.ManyToManyField(Categoria, related_name="pedido", blank=True, null=True)
    def __str__(self):
        return f"({self.id}) {self.data} "
class Meta:
    verbose_name = "Pedido"
    verbose_name_plural = "Pedidos"