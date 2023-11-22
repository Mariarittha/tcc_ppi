from django.urls import path
from . import views

app_name = "filomenas"

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    # logado
    path('home/', views.Home.as_view(), name='home'),
    path('pacote/', views.pacote.as_view(), name='pacote'),

    # nao logado
    path('home2/', views.Home2.as_view(), name='home2'),
    path('pacote2/', views.pacote2.as_view(), name='pacote2'),

    # filomenas
    path('filomenas/', views.filomenas.as_view(), name='filomenas'),


]