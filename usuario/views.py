from django.shortcuts import render

# Create your views here.
from urllib import request
from django.contrib import messages
from multiprocessing import context
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Usuario
from usuario.forms import usuarioForm, usuarioSysForm
from django.contrib.auth import login
from django.contrib.messages.views import SuccessMessageMixin
from main import urls
from braces.views import GroupRequiredMixin

#Listagem dos Usuários
class listagemUsuariosView(ListView):
    model = Usuario
    queryset = Usuario.objects.all().order_by('nome')


#Cadastro dos Usuários
class usuarioCreateView(GroupRequiredMixin,SuccessMessageMixin,CreateView):
    model = Usuario
    group_required = u"coord"
    form_class = usuarioForm
    success_url = '/usuarios/novo/register'
    success_message = "Cadastrado com sucesso"


    def get_success_message(self, cleaned_data):
        return self.success_message 
#Editar Usuários

class usuarioUpdateView(GroupRequiredMixin,UpdateView):
    model = Usuario
    group_required = u"coord"
    form_class = usuarioForm
    success_url = '/usuarios/'

#Excluir Usuários

class usuarioDeleteView(GroupRequiredMixin,DeleteView):
    model = Usuario
    group_required = u"coord"
    success_url = '/usuarios/'


def register(request):
    if request.method=="POST":
        form = usuarioSysForm(request.POST)
        
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        
        if len(password1)<8:
            messages.error(request, 'A senha deve ter 8 caracteres')
        if password1 != password2:  
            messages.error(request,"As senhas são diferentes")  
        
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Login Registrado com Sucesso')
            return redirect('home') 
        messages.error(request, 'Falha no registro')
    form = usuarioSysForm()
    context = {'form': form}
    return render(request, template_name='usuario/register.html', context=context)