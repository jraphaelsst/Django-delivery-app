from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.home, name='home'),
    path("categoria/<int:id>", views.categorias, name='categoria'),
    path("produto/<int:id>", views.produtos, name='produto'),
    path('add_carrinho/', views.add_carrinho, name='add_carrinho'),
    path('ver_carrinho/', views.ver_carrinho, name='ver_carrinho'),
    path('remover_produto/<int:id>', views.remover_produto, name='remover_produto'),
]