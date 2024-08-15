from django.db import models
from .estado import Estado


class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT, related_name="cidade", null=True, blank=True)
    def __str__(self):
        return f"({self.id}) {self.nome}-{self.estado} "
class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"