from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.messages import constants
from .models import User
import re
from .utils import password_is_valid
from django.contrib import auth


def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_senha = request.POST.get('confirmar_senha')

        if len(username.strip()) == 0 or len(email.strip()) == 0 or len(password.strip()) == 0:
            messages.add_message(
                request, constants.ERROR, 'Ops! Por favor preencha todos os dados corretamente!')
            return redirect('/auth/cadastro')

        if password != confirm_senha:
            messages.add_message(request, constants.ERROR,
                                 'As senhas não coincidem!')
            return redirect('/auth/cadastro')

        if not "." in email:
            messages.add_message(
                request, constants.ERROR, 'Ops! Por favor preencha seu e-mail corretamente!')

            return redirect('/auth/cadastro')

        usuario = User.objects.filter(username=username)

        if usuario.exists():
            messages.add_message(
                request, constants.ERROR, 'Ops! Por Já existe um usuário com este nome!')
            return redirect('/auth/cadastro')

        mail = User.objects.filter(email=email)

        if mail.exists():
            messages.add_message(
                request, constants.ERROR, 'Ops! Este e-mail já está cadastrado no sistema!')
            return redirect('/auth/cadastro')

        checar_senhar = password_is_valid(request, password)
        if not checar_senhar:
            return redirect('/auth/cadastro')

        try:
            user = User.objects.create_user(  # type: ignore
                username=username,
                email=email,
                password=password
            )
            user.save()
            messages.add_message(request, constants.SUCCESS,
                                 'Usuário cadastrado com sucesso!')
            return redirect('/auth/logar')

        except Exception as error:
            messages.add_message(request, constants.ERROR,
                                 f'O erro encontrado foi {error.__class__}')
            return redirect('/auth/cadastro')


def logar(request):
    if request.method == "GET":
        return render(request, 'logar.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)

        if not user:
            messages.add_message(request, constants.ERROR,
                                 'Ops! Usuário ou senha inválidos!')
            return redirect('/auth/logar')
        else:
            auth.login(request, user)
            return redirect("/adote/divulgar")


def sair(request):
    auth.logout(request)
    messages.add_message(request, constants.INFO,
                         'Obrigado por passar um tempo conosco. Volte sempre!')
    return redirect('/auth/logar')
