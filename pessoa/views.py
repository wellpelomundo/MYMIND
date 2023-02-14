from django.shortcuts import render, redirect
from .models import Avaliacao_diaria, Acontecimento, Alertas_crises
from django.contrib import messages
from django.contrib.messages import constants
from usuarios.models import Usuario
from django.http import HttpResponse


def home(request):
    if request.session.get('usuario'):
        
        if request.method == 'GET':
            usuario = Usuario.objects.get(id = request.session['usuario'])
            avaliacoes = Avaliacao_diaria.avaliacao
            alerta = Alertas_crises.alertas
                       
            return render(request,'home.html', {'usuario':usuario, 'avaliacoes':avaliacoes, 'alerta':alerta, })
    else:
        messages.add_message(request, constants.ERROR, 'Você precisa estar logado para acessar.')
        return redirect('/auth/login/')   


def s_avaliacao(request):
    if request.method == "POST":
            usuario = Usuario.objects.get(id = request.session['usuario'])
            estado_mental = request.POST.getlist('estado_mental')[0]                                            

            atendimento = Avaliacao_diaria(
                 usuario = usuario,
                 estado_mental = estado_mental
                 )

            atendimento.save()
            messages.success(request, 'Resgistro Adicionado ')
            return redirect('/pessoa/home/')

def s_anotacao(request):
     if request.method == "POST":
            usuario = Usuario.objects.get(id = request.session['usuario'])
            acontecimento_negativo = request.POST.get('acontecimento_negativo')
            acontecimento_positivo = request.POST.get('acontecimento_positivo')                                            

            atendimento = Acontecimento(
                usuario = usuario,
                acontecimento_negativo = acontecimento_negativo,
                acontecimento_positivo = acontecimento_positivo,
                )

            atendimento.save()
            messages.success(request, 'Resgistro Adicionado ')
            return redirect('/pessoa/home/')
    
    
def s_alerta(request):
    if request.method == "POST":
            usuario = Usuario.objects.get(id = request.session['usuario'])
            alerta_crises = request.POST.getlist('alerta_crises')[0]
            data_acontecimento = request.POST.get('data_acontecimento')
            data_superacao = request.POST.get('data_superacao')
                                            

            atendimento = Alertas_crises(
                usuario = usuario,
                alerta_crises = alerta_crises,
                data_acontecimento = data_acontecimento,
                data_superacao = data_superacao,

            )

            atendimento.save()
            messages.success(request, 'Resgistro Adicionado ')
            return redirect('/pessoa/home/')
    

def registro(request):
    if request.session.get('usuario'):         
        usuario = Usuario.objects.get(id = request.session['usuario'])
        avaliacao = Avaliacao_diaria.objects.filter(usuario = usuario)
        registro = Acontecimento.objects.filter(usuario = usuario)
        alerta = Alertas_crises.objects.filter(usuario = usuario)
                    
        return render(request,'registro.html', {'usuario': usuario,'avaliacao': avaliacao, 'registro': registro, 'alerta':alerta, })
    else:
        messages.add_message(request, constants.ERROR, 'Você precisa estar logado para acessar.')
        return redirect('/auth/login/')
  


