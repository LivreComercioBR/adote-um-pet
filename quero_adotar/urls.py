from django.urls import path
from quero_adotar import views


urlpatterns = [
    path('listar_pets/', views.listar_pets,  # type: ignore
         name='listar_pets'),  # type: ignore
    path('ver_pet/<int:id>', views.ver_pet, name="ver_pet"),  # type: ignore
    path('solicitar_adocao/<int:id>',
         views.solicitar_adocao, name='solicitar_adocao'),
    path('processa_pedido_adocao/<int:id_pedido>', views.processa_pedido_adocao,  # type: ignore
         name='processa_pedido_adocao'),  # type: ignore
    path('dashboard/', views.dashboard, name="dashboard"),
    path('mostrar_grafico/', views.mostrar_grafico, name="mostrar_grafico"),
]
