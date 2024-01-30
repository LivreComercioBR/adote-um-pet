from datetime import datetime
import re
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from adocao.models import Pet, Raca
from adote_app.models import User
from quero_adotar.models import PedidoAdocao
from django.contrib import messages
from django.contrib.messages import constants
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt


def listar_pets(request):
    if request.method == "GET":
        pets = Pet.objects.filter(status="P")
        racas = Raca.objects.all()

        cidade = request.GET.get("cidade")
        raca_filter = request.GET.get("raca")

        if cidade:
            pets = pets.filter(cidade__icontains=cidade)

        if raca_filter:
            pets = pets.filter(raca_id=raca_filter)
            raca_filter = Raca.objects.get(id=raca_filter)

        return render(request, 'listar_pets.html', {'pets': pets, 'racas': racas, 'cidade': cidade, 'raca_filter': raca_filter})


def ver_pet(request, id):
    if request.method == "GET":
        pet = Pet.objects.get(id=id)
        return render(request, 'ver_pet.html', {'pet': pet})


def solicitar_adocao(request, id):
    pet = Pet.objects.filter(id=id).filter(status="P")

    if not pet.exists():
        messages.add_message(request, constants.ERROR,
                             'Este Pet não está mais disponível!')
        return redirect('quero_adotar/listar_pets')

    pedido = PedidoAdocao(pet=pet.first(),
                          usuario=request.user,
                          data=datetime.now(),)
    pedido.save()
    messages.add_message(request, constants.SUCCESS,
                         'Pedido enviado com sucesso! Por favor, aguarde retorno do usuário.')
    return redirect('/quero_adotar/listar_pets')


def processa_pedido_adocao(request, id_pedido):
    if request.method == "GET":
        status = request.GET.get('status')

        pedido = PedidoAdocao.objects.get(id=id_pedido)

        pet = Pet.objects.filter(id=pedido.pet_id)

        if status == "A":
            pedido.status = "AP"
            resposta = 'Olá, seu pedido de adoção foi aprovado! Parabéns!'

        elif status == "R":
            pedido.status = "R"
            resposta = 'Olá, lamentamos mas o seu pedido de adoção foi recusado!'

        pedido.save()

        for statu in pet:
            statu.status = "A"
            statu.save()

        # def send_mail(subject, message, from_email, recipient_list):
        #     return True

        meu_email = send_mail(

            subject="Status do seu pedido de adoção",
            message="Seu pedido foi aceito! Parabéns!",
            from_email="ronaldocorreiadesouza@gmail.com",
            recipient_list=[pedido.usuario.email,],)
        messages.add_message(request, constants.SUCCESS,
                             "Pedido de adoção processado com sucesso!")

        return redirect('/quero_adotar/listar_pets/')


@csrf_exempt
def dashboard(request):
    return render(request, 'dashboard.html')


@csrf_exempt
def mostrar_grafico(request):
    if request.method == "GET":
        racas = Raca.objects.all()

        qtd_adocoes = []
        for raca in racas:
            adocoes = PedidoAdocao.objects.filter(pet__raca=raca).count()
            qtd_adocoes.append(adocoes)

        racas = [raca.raca for raca in racas]
        data = {'qtd_adocoes': qtd_adocoes,
                'labels': racas}

        return JsonResponse(data)
