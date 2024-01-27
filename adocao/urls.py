from django.urls import path
from adocao import views


urlpatterns = [
    path('divulgar/', views.divulgar, name='divulgar'),  # type: ignore
]
