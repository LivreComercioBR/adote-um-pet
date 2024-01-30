from django.db import models
from adocao.models import Pet
from adote_app.models import User


class PedidoAdocao(models.Model):
    choices_status = (
        ('AG', 'Aguardando aprovação'),
        ('AP', 'Aprovado'),
        ('R', 'Recusado')
    )

    pet = models.ForeignKey(Pet, on_delete=models.DO_NOTHING)  # type: ignore
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    data = models.DateTimeField()
    status = models.CharField(
        max_length=2, choices=choices_status, default='AG')

    def __str__(self) -> str:
        return self.pet.nome
