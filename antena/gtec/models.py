from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
import uuid

class Vaga(models.Model):
    id = models.IntegerField('ID', primary_key = True, help_text= 'ID único para essa vaga') # editable = False 'esconde' o campo do id, evitando que ele seja editado
    hora_dev = models.DateField('Hora de Devolução', null = True, blank = True)

    STATUS_VAGA = (
        ('o', 'Ocupada'),
        ('d', 'Desocupada'),
    )

    status = models.CharField(
        max_length = 1,
        choices = STATUS_VAGA,
        blank = True,
        default = 'd',
        help_text = 'Disponibilidade da vaga'
    )

    class Meta:
        verbose_name = "Vaga"
        verbose_name_plural = 'Vaga'
        ordering = ['id'] # Como vão ser ordenadas as vagas. Tentar ordenar pelo status depois!

    def __str__(self):
        return str(self.id)

class Cliente(models.Model):
    nome = models.CharField("Nome", max_length = 50)
    sobrenome = models.CharField("Sobrenome", max_length = 80)
    cpf = models.CharField("CPF", help_text="Digite apenas números", max_length=12)
    telefone = PhoneNumberField("Telefone", max_length = 14, null=False, blank=False, unique=True)
    email = models.EmailField("E-mail", blank=True, unique=True)
    creditos = models.DecimalField("Créditos", max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Cliente"

    def __str__(self):
        return self.nome

class Reserva(models.Model):
    nome_pessoa = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    cpf = models.CharField("CPF", help_text="Digite apenas numeros", max_length=12, blank=True)
    valor = models.CharField("Valor da vaga", max_length=30, null=True)
    hora_operacao = models.DateTimeField("Hora da operação", null=True)
    hora_prevista_saida = models.DateTimeField("Hora prevista para saída", null=True)
    debito_id = models.UUIDField(default=uuid.uuid4) #não pode ter mais uma primary key
    id_vaga = models.UUIDField(primary_key=True, default=uuid.uuid4)
    hora_saida = models.DateTimeField("Hora da saída", null=True)

    class Meta:
        verbose_name = "Reserva de vagas"
        verbose_name_plural = "Reserva de vagas"

    def __str__(self):
        return ("Reserva do " + self.nome_pessoa.nome)
