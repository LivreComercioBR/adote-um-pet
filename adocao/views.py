from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.messages import constants
from adocao.models import Pet, Raca, Tag


def divulgar(request):
    if request.method == "GET":
        tags = Tag.objects.all()
        raca = Raca.objects.all()
        return render(request, 'divulgar.html', {"racas": raca, "tags": tags})
    elif request.method == "POST":
        foto = request.FILES.get('foto')
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        estado = request.POST.get('estado')
        cidade = request.POST.get('cidade')
        telefone = request.POST.get('telefone')
        tags = request.POST.getlist('tags')
        raca = request.POST.get('raca')

        if len(nome.strip()) == 0 or len(descricao.strip()) == 0 or len(estado.strip()) == 0 or len(cidade.strip()) == 0 or len(telefone.strip()) == 0:

            messages.add_message(
                request, constants.ERROR, 'Por favor preencha todos os dados corretamente!')
            return redirect('/adote/divulgar')

        if not nome or not raca or not tags:
            messages.add_message(
                request, constants.ERROR, 'Por favor preencha todos os dados corretamente!')
            return redirect('/adote/divulgar')

        try:
            pet = Pet(
                usuario=request.user,
                foto=foto,
                nome=nome,
                descricao=descricao,
                estado=estado,
                cidade=cidade,
                telefone=telefone,
                raca_id=raca,
            )
            pet.save()

            # for tag_id in tags:
            #     tag = Tag.objects.get(id=tag_id)
            #     pet.tags.add(tag)

            # pet.save()
            # messages.add_message(request, constants.SUCCESS,
            #                      'Pet cadastrado com sucesso!')
            return redirect('/')

        except Exception as error:
            messages.add_message(request, constants.ERROR,
                                 f'A causa do erro foi {error.__cause__}')
            return redirect('/adote/divulgar')
