from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.messages import constants
from .models import Usuario
from hashlib import sha256
from django.http import HttpResponse

def login(request):
    if request.session.get('usuario'):
        return redirect('/pessoa/home/')
   
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        senha = sha256(senha.encode()).hexdigest()

        usuario = Usuario.objects.filter(email = email).filter(senha = senha)

        if len(usuario) == 0:
            messages.add_message(request, constants.ERROR, 'Usuario ou senha incorreta')
            return render(request, 'login.html')
        elif len(usuario) > 0:
            request.session['usuario'] = usuario[0].id
            return redirect('/pessoa/home')
        
def cadastro(request):
    if request.session.get('usuario'):
        return redirect('/pessoa/home/')
   
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
            

        usuario = Usuario.objects.filter(email = email)

        if len(nome.strip()) == 0 or len(email.strip()) == 0 or len(senha.strip()) == 0:
            messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
            return render(request, 'cadastro.html')
        
        if len(senha) < 6:
            messages.add_message(request, constants.ERROR, 'Sua senha deve ter pelos menos 8 caracteres')
            return render(request, 'cadastro.html')    
               
        if len(usuario) > 0:
            messages.add_message(request, constants.ERROR, 'Usuario ja existe no sistema')
            return render(request, 'login.html')
        
        try:
            senha = sha256(senha.encode()).hexdigest()
            usuario = Usuario(
                nome=nome,
                email=email,
                senha=senha
            )
            usuario.save()

            messages.add_message(request, constants.SUCCESS, 'Cadastro realizado com sucesso!!')
            return render(request, 'login.html')
        except:
            messages.add_message(request, constants.ERROR, 'Todo mundo erra e dessa vez fomos nós')
            return render(request, 'cadastro.html')

def sair(request):
    request.session.flush()
    return redirect('/auth/login/')