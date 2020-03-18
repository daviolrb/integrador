from django.urls import path
from gtec.views import IndexTemplateView, VagaListView, VagaUpdateView, VagaCreateView, VagaDeleteView, ClienteCreateView, \
ClienteListView, ClienteUpdateView, ClienteDeleteView, ReservaCreateView, ReservaListView, ReservaUpdateView, ReservaDeleteView

app_name = 'gtec'

urlpatterns = [
	path('', IndexTemplateView.as_view(), name="index"),

	path('vagas/criar/', VagaCreateView.as_view(), name="cadastra_vaga"),

    path('vagas/', VagaListView.as_view(), name="lista_vaga"),

    path('vagas/<pk>', VagaUpdateView.as_view(), name="atualiza_vaga"),

    path('vagas/excluir/<pk>/', VagaDeleteView.as_view(), name="deleta_vaga"),

    path('clientes/criar/', ClienteCreateView.as_view(), name="cria_cliente"),

    path('clientes/', ClienteListView.as_view(), name="lista_cliente"),

    path('clientes/<pk>', ClienteUpdateView.as_view(), name="atualiza_cliente"),

    path('clientes/excluir/<pk>/', ClienteDeleteView.as_view(), name="deleta_cliente"),

    path('reserva/criar/', ReservaCreateView.as_view(), name="cria_reserva"),

    path('reserva/', ReservaListView.as_view(), name="lista_reserva"),

    path('reserva/<pk>', ReservaUpdateView.as_view(), name="atualiza_reserva"),

    path('reserva/excluir/<pk>/', ReservaDeleteView.as_view(), name="deleta_reserva"),

]
