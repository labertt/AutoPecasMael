from django.urls import path

from peca.views import PecaCreateView, ListaPecaView, PecaUpdateView, PecaDeleteView

urlpatterns = [
    path('', ListaPecaView.as_view(), name='peca.index'),
    path('novo', PecaCreateView.as_view(), name='peca.novo'),
    path('editar/<int:pk>', PecaUpdateView.as_view(), name='peca.editar'),
    path('excluir/<int:pk>', PecaDeleteView.as_view(), name='peca.excluir'),
]