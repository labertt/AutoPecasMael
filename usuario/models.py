from django.db import models
from .validator import validateCpf, validateDate, validateEmail, validateEndereco, validateNoDigits, validateNome, validateSenha

class Usuario(models.Model):
    choices_usuario_cargo = (
        ('Gerente','Gerente'),
        ('Funcionario','Funcionario')
    )


    nome = models.CharField(max_length=100, blank=False, null=True, validators=[validateNome, validateNoDigits])
    email = models.CharField(max_length=100, blank=False, null=True, unique=True, validators=[validateEmail])
    cpf = models.CharField(max_length=11, blank=False, null=True, unique=True, validators=[validateCpf])
    endereco = models.CharField(max_length=100, blank=False, null=True, validators=[validateEndereco])
    data_nascimento = models.DateField(validators=[validateDate])
    usernome = models.CharField(max_length=40, blank=False, null=True, unique=True)
    cargo = models.CharField(max_length=50, blank=False, null=True, choices=choices_usuario_cargo)

    def __str__(self):
        return self.nome