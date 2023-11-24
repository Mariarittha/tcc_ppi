from django.urls import path
from . import views

app_name = "filomenas"

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    # logado
    path('home/', views.Home.as_view(), name='home'),
    path('pacote/', views.pacote.as_view(), name='pacote'),
    path('filomenas/', views.filomenas.as_view(), name='filomenas'),

    # nao logado
    path('home2/', views.Home2.as_view(), name='home2'),
    path('pacote2/', views.pacote2.as_view(), name='pacote2'),
    path('filomenas2/', views.filomenas2.as_view(), name='filomenas2'),

    # filomenas
    path('filomenas/', views.filomenas.as_view(), name='filomenas'),

    # hopede
    path('perfil/', views.hospede.as_view(), name='perfil'),

    # outros
    path('form/', views.CriarEstadia.as_view(), name='criar'),
    path('listar/', views.ListarEstadia.as_view(), name='listar'),
    path('comprar/', views.comprar.as_view(), name='comprar'),

]