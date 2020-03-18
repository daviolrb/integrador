from django import forms
from .models import Post, Vaga, Cliente, Reserva

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'body', 'author', 'status']

class InsereVagaForm(forms.ModelForm):
	class Meta:
		model = Vaga
		fields = ['id', 'hora_dev', 'status']

class InsereClienteForm(forms.ModelForm):
	class Meta:
		model = Cliente
		fields = ['nome', 'sobrenome', 'cpf', 'telefone', 'email', 'creditos']

class InsereReservaForm(forms.ModelForm):
	class Meta:
		model = Reserva
		fields = ['nome_pessoa', 'cpf', 'valor', 'hora_operacao', 'hora_prevista_saida', 'debito_id', 'id_vaga', 'hora_saida']

class VagaCreate(forms.ModelForm):
    class Meta:
        model = Vaga
        fields = '__all__'