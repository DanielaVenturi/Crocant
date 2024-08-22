from django.db import models
# from django.contrib.auth.models import User
from .cidade import Cidade

class Endereco(models.Model):
    rua = models.CharField(max_length=255)
    cep = models.PositiveIntegerField()
    cidades = models.ForeignKey(Cidade,on_delete=models.PROTECT, related_name="cidades", null=True, blank=True)
    # usuario = models.ForeignKey(User, on_delete=models.PROTECT, related_name="cidades", null=True, blank=True)

    def __str__(self):
        return f"({self.id}) {self.rua}-{self.cep}-{self.cidades} "
      
    class Meta:
        verbose_name = "Endereco"
        verbose_name_plural = "Enderecos"
        