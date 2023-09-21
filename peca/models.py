from django.db import models
from .validator import validateCodBarras, validateNoDigits, validateNome, validatePreco

class Peca(models.Model):
    nome_peca = models.CharField(max_length=40, validators=[validateNome])
    marca_peca = models.CharField(max_length=40)
    valor_peca = models.FloatField(validators=[validatePreco])
    codigo_barras_peca = models.CharField(max_length=13, validators=[validateCodBarras])
    disponibilidade_peca = models.BooleanField()

    def __str__(self) -> str:
        return str(self.nome_peca)