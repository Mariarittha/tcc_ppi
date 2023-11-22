from django.contrib import messages
from django.views.generic import ListView,CreateView,DeleteView,DetailView, UpdateView,TemplateView
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.messages import views

# não logado

class Home(generic.TemplateView):
    template_name = "nao_logado/home.html"

class pacote(generic.TemplateView):
    template_name = "nao_logado/pacote.html"

class filomenas(generic.TemplateView):
    template_name = "nao_logado/filomenas.html"

# logado

class Home2(generic.TemplateView):
    template_name = "logado/home.html"

class pacote2(generic.TemplateView):
    template_name = "logado/pacote.html"

class filomenas2(generic.TemplateView):
    template_name = "logado/filomenas.html"

#filomenas

class filomenas(generic.TemplateView):
    template_name = "filomenas/filomenas.html"

class Index(generic.TemplateView):
    template_name = "filomenas/index.html"