from django.db import models
from datetime import date, timedelta
from usuarios.models import Usuario

data_limite_50_anos = date.today() - timedelta(days=365 * 50)

class Avaliacao_diaria(models.Model):

    avaliacao = (
        ('P', 'PÉSSIMO'),
        ('R', 'RUIM'),
        ('B', 'BOM'),
        ('E', 'EXCELENTE'),
    )
    estado_mental = models.CharField(
        "Selecione o seu estado mental atual", max_length=2, choices=avaliacao)
    data = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)

    
class Acontecimento(models.Model):
    acontecimento_negativo = models.TextField(
        'Acontecimento Negativo', max_length=100)
    acontecimento_positivo = models.TextField(
        'Acontecimento Positivo', max_length=100)
    data = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)

    
class Alertas_crises(models.Model):

    alertas = (
        ('P', 'PANICO'),
        ('A', 'ANSIEDADE'),
        ('D', 'DEPRESSAO'),
    )

    alerta_crises = models.CharField(
        "Selecione o seu estado de crise", max_length=2, choices=alertas)
    data_atual = models.DateTimeField(auto_now=True)
    data_acontecimento = models.DateField(default=data_limite_50_anos, max_length=50)
    data_superacao = models.DateField(default=data_limite_50_anos, max_length=50)
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
  