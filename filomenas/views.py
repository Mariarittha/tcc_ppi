from django.contrib import messages
from django.views.generic import ListView,CreateView,DeleteView,DetailView, UpdateView,TemplateView
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.messages import views
from django.contrib.auth.mixins import LoginRequiredMixin
from requests import request
from .forms import EstadiaForm, ProdutosForm, HospedeForm, FilomenasForm
from .models import estadia, Produtos, filomenas, hospede

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


# hospede

class hospede(generic.TemplateView):
    template_name = "hospede/perfil.html"

class comprar( generic.TemplateView, LoginRequiredMixin):
    template_name = "hospede/perfilc.html"
    
    
# CRUD de Estadia
class ListarEstadia(LoginRequiredMixin, generic.ListView):
    model = estadia
    template_name = 'logado/pacote.html'
    context_object_name = 'estadias'
    paginate_by = 5
    
class ListarEstadia2(LoginRequiredMixin, generic.ListView):
    model = estadia
    template_name = 'nao_logado/pacote.html'
    context_object_name = 'estadias'
    paginate_by = 5

class DetalharEstadia(generic.DetailView):
    model = estadia

class CriarEstadia(LoginRequiredMixin, views.SuccessMessageMixin, generic.CreateView):
    model = estadia
    form_class = EstadiaForm
    template_name = 'filomenas/form_estadia.html'
    success_url = reverse_lazy("filomenas:index")
    success_message = "Estadia cadastrada com sucesso!"

class AtualizarEstadia(LoginRequiredMixin, views.SuccessMessageMixin, generic.UpdateView):
    model = estadia
    form_class = EstadiaForm
    success_url = reverse_lazy("reservas:index")
    success_message = "Estadia atualizada com sucesso!"

class ApagarEstadia(LoginRequiredMixin, generic.DeleteView):
    model = estadia
    success_url = reverse_lazy("reservas:index")
    
    
# CRUD de perfil do hospede 

class Detalharhospede(generic.DetailView):
    model = hospede

class Criarhospede(LoginRequiredMixin, views.SuccessMessageMixin, generic.CreateView):
    model = hospede
    form_class = HospedeForm
    template_name = 'hospede/form_hospede.html'
    success_url = reverse_lazy("filomenas:index")
    success_message = "Hospede cadastrado com sucesso!"

class Atualizarhospede(LoginRequiredMixin, views.SuccessMessageMixin, generic.UpdateView):
    model = hospede
    form_class = HospedeForm
    success_url = reverse_lazy("reservas:index")
    success_message = "Perfil atualizado com sucesso, {{ request.user.username }}!" 

class Apagarhospede(LoginRequiredMixin, generic.DeleteView):
    model = hospede
    success_url = reverse_lazy("reservas:index")
    
# CRUD de perfil filomenas

class Detalharfilomena(generic.DetailView):
    model = hospede

class Criarfilomena(LoginRequiredMixin, views.SuccessMessageMixin, generic.CreateView):
    model = filomenas
    form_class = FilomenasForm
    template_name = 'filomenas/form_filomenas.html'
    success_url = reverse_lazy("filomenas:index")
    success_message = "filomena cadastrada com sucesso!"

class Atualizarfilomena(LoginRequiredMixin, views.SuccessMessageMixin, generic.UpdateView):
    model = filomenas
    form_class = FilomenasForm
    success_url = reverse_lazy("reservas:index")
    success_message = "Perfil atualizado com sucesso, {{ request.user.username }}!" 

class Apagarfilomena(LoginRequiredMixin, generic.DeleteView):
    model = filomenas
    success_url = reverse_lazy("reservas:index")