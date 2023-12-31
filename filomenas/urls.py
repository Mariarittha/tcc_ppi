from django.urls import path
from . import views

app_name = "filomenas"

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    # logado
    path('home/', views.Home.as_view(), name='home'),
    path('pacote/', views.pacote.as_view(), name='pacote'),
    path('filomenas/', views.filomenas.as_view(), name='filomenas'),
    path('detalhar/<int:pk>/', views.DetalharEstadia.as_view(), name='detalhar'),


    # nao logado
    path('home2/', views.Home2.as_view(), name='home2'),
    path('pacote2/', views.pacote2.as_view(), name='pacote2'),
    path('filomenas2/', views.filomenas2.as_view(), name='filomenas2'),
    path('listar2/', views.ListarEstadia2.as_view(), name='listar2'),
    path('detalhar2/<int:pk>/', views.DetalharEstadia2.as_view(), name='detalhar2'),



    # filomenas
    path('filomenas/', views.filomenas.as_view(), name='filomenas'),
    path('form_filomenas/', views.Criarfilomena.as_view(), name='form_filomenas'),
    path('detalharfilo/<int:pk>/', views.Detalharfilomena.as_view(), name='detalharfilo'),

    # hopede
    path('perfil/', views.hospede.as_view(), name='perfil'),
    path('form_hospede/', views.Criarhospede.as_view(), name='form_hospede'),


    # outros
    path('form/', views.CriarEstadia.as_view(), name='criar'),
    path('listar/', views.ListarEstadia.as_view(), name='listar'),
    path('comprar/', views.comprar.as_view(), name='comprar'),

]