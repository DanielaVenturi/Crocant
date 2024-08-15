from django.db import models


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=7, decimal_places=2, default=0, null=True, blank=True)
    def __str__(self):
        return f"({self.id}){self.nome} {self.preco} "
class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"