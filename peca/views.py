from django.shortcuts import render
from .models import Peca
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import PecaForm

class ListaPecaView(ListView):
    model = Peca
    queryset = Peca.objects.all().order_by('nome_peca')

    def get_queryset(self):
        queryset = super().get_queryset()

        filto_nome = self.request.GET.get('nome') or None
        if filto_nome:
            queryset = queryset.filter(nome_peca__contains=filto_nome)
        return queryset

class PecaCreateView(CreateView):
    model = Peca
    form_class = PecaForm
    success_url = '/pecas/'

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class PecaUpdateView(UpdateView):
    model = Peca
    form_class = PecaForm
    success_url = '/pecas/'

class PecaDeleteView(DeleteView):
    model = Peca
    success_url = '/pecas/'