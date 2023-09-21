from django.forms import ValidationError, fields, models
from django import forms
from .models import Usuario
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, AbstractUser

class usuarioForm (forms.ModelForm):
    data_nascimento = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    
    class Meta:
        model = Usuario
        fields = ['nome',
                'email',
                'cpf',
                'endereco',
                'data_nascimento',
                'usernome',
                'cargo']


class usuarioSysForm(UserCreationForm):
    username = forms.ChoiceField(choices=[('0','--Selecione o Username--')]+[(Usuario.usernome, Usuario.usernome) for Usuario in Usuario.objects.all()])
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)  
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)  
    class Meta:
        model = User
        fields = ('username','password1','password2')
        help_texts = {k:"" for k in fields}


    def save(self, commit=True):
        user = super(usuarioSysForm, self).save(commit=False)

        if commit:
            user.save()
        return user