from . import views
from django.urls import path, include

urlpatterns = [
    path('finalizar_pedido/', views.finalizar_pedido, name='finalizar_pedido'),
    path('validaCupom', views.validaCupom, name='validaCupom'),
]