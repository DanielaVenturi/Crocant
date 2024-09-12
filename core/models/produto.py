from django.db import models
from .categoria import Categoria
from uploader.models import Image
TAMANHOS_CHOICES = [
    (33,'33'),
    (34, '34'),
    (35, '35'),
    (36, '36'),
    (37, '37'),
    (38, '38'),
    (39, '39'),
    (40, '40'),
    (41, '41'),
    (42, '42'),
    (43, '43'),
    (44, '44'),
]

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    tamanho = models.PositiveIntegerField(choices=TAMANHOS_CHOICES, null=True, blank=True)
    preco = models.DecimalField(max_digits=7, decimal_places=2, default=0, null=True, blank=True)
    categoria = models.ManyToManyField(Categoria, related_name="produto", blank=True)
    capa = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None,)
    
    def __str__(self):
        return f"({self.id}){self.nome} {self.preco} "
    
class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"