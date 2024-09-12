from django.db import models
from django.contrib.auth import get_user_model
from .cidade import Cidade

User = get_user_model() 

class Endereco(models.Model):
    rua = models.CharField(max_length=255)
    cep = models.PositiveIntegerField()
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT, related_name="cidades", null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="enderecos", null=True, blank=True)

    def __str__(self):
        return f"({self.id}) {self.rua}-{self.cep}-{self.cidade}"

    class Meta:
        verbose_name = "Endereço"
        verbose_name_plural = "Endereços"