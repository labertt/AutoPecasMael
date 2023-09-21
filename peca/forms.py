from django import forms
from .models import Peca

class PecaForm(forms.ModelForm):
    class Meta:
        model = Peca
        fields = ['nome_peca', 'marca_peca', 'valor_peca', 'codigo_barras_peca', 'disponibilidade_peca']