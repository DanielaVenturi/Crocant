from django.db import models


class Estado(models.Model):
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=2)
    
    @property
    def sigla_maiusculo(self):
        return self.sigla.upper()
    def __str__(self):
        return f"({self.id}) {self.nome}-{self.sigla_maiusculo} "
class Meta:
        verbose_name = "Estado"
        verbose_name_plural = "Estados"