from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return f"({self.id}) {self.nome} "
class Meta:
        verbose_name = "Categororia"
        verbose_name_plural = "Categorias"