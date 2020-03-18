from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.views import generic
from django.urls import reverse_lazy
from .models import Vaga, Cliente, Reserva
from .forms import InsereVagaForm, InsereClienteForm, InsereReservaForm, VagaCreate

class IndexTemplateView(TemplateView):
    template_name = "gtec/index.html"

# VAGAS
class VagaListView(ListView):
    template_name = "gtec/lista.html"
    model = Vaga
    context_object_name = "vaga"

@method_decorator(login_required, name='dispatch')
class VagaCreateView(CreateView):
    template_name = "gtec/cria.html"
    model = Vaga
    form_class = InsereVagaForm
    success_url = reverse_lazy("gtec:lista_vaga")

@method_decorator(login_required, name='dispatch')
class VagaUpdateView(UpdateView):
    template_name = "gtec/atualiza.html"
    model = Vaga
    fields = '__all__'
    context_object_name = 'vaga'
    success_url = reverse_lazy("gtec:lista_vaga")

@method_decorator(login_required, name='dispatch')
class VagaDeleteView(DeleteView):
    template_name = "gtec/exclui.html"
    model = Vaga
    context_object_name = 'vaga'
    success_url = reverse_lazy("gtec:lista_vaga")

# CLIENTES
class ClienteListView(ListView):
    template_name = "gtec/lista_cliente.html"
    model = Cliente
    context_object_name = "cliente"

class ClienteCreateView(CreateView):
    template_name = "gtec/cria_cliente.html"
    model = Cliente
    form_class = InsereClienteForm
    success_url = reverse_lazy("gtec:lista_cliente")

@method_decorator(login_required, name='dispatch')
class ClienteUpdateView(UpdateView):
    template_name = "gtec/atualiza_cliente.html"
    model = Cliente
    fields = '__all__'
    context_object_name = 'cliente'
    success_url = reverse_lazy("gtec:lista_cliente")

@method_decorator(login_required, name='dispatch')
class ClienteDeleteView(DeleteView):
    template_name = "gtec/exclui_cliente.html"
    model = Cliente
    context_object_name = 'cliente'
    success_url = reverse_lazy("gtec:lista_cliente")

# RESERVA DE VAGAS
class ReservaListView(ListView):
    template_name = "gtec/lista_reserva.html"
    model = Reserva
    context_object_name = "reserva"

@method_decorator(login_required, name='dispatch')
class ReservaCreateView(CreateView):
    template_name = "gtec/cria_reserva.html"
    model = Reserva
    form_class = InsereReservaForm
    success_url = reverse_lazy("gtec:lista_reserva")

@method_decorator(login_required, name='dispatch')
class ReservaUpdateView(UpdateView):
    template_name = "gtec/atualiza_reserva.html"
    model = Reserva
    fields = '__all__'
    context_object_name = 'reserva'
    success_url = reverse_lazy("gtec:lista_reserva")

@method_decorator(login_required, name='dispatch')
class ReservaDeleteView(DeleteView):
    template_name = "gtec/exclui_cliente.html"
    model = Reserva
    context_object_name = 'reserva'
    success_url = reverse_lazy("gtec:lista_reserva")