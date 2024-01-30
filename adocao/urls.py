from django.urls import path
from adocao import views
from django.core.mail import send_mail


urlpatterns = [
    path('divulgar/', views.divulgar, name='divulgar'),  # type: ignore
    path('meu_pet/', views.meu_pet, name='meu_pet'),  # type: ignore
    path('remover_pet/<int:id>', views.remover_pet, name="remover_pet"),
    path('ver_pedido_adocao/', views.ver_pedido_adocao,  # type: ignore
         name="ver_pedido_adocao"),  # type: ignore


]
