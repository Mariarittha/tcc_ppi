from django.contrib import messages
from django.views.generic import ListView,CreateView,DeleteView,DetailView, UpdateView,TemplateView
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.messages import views
from django.contrib.auth.mixins import LoginRequiredMixin
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
    
    
# CRUD de Estadia
class EstadiaListView(LoginRequiredMixin, generic.ListView):
    model = estadia
    paginate_by = 5

class ReservaDetailView(LoginRequiredMixin, generic.DetailView):
    model = estadia

class ReservaCreateView(LoginRequiredMixin, views.SuccessMessageMixin, generic.CreateView):
    model =  estadia
    form_class = EstadiaForm
    success_url = reverse_lazy("reservas:reservas-list")
    success_message = "Reserva cadastrada com sucesso!"

class ReservaUpdateView(LoginRequiredMixin, views.SuccessMessageMixin, generic.UpdateView):
    model = estadia
    form_class = EstadiaForm
    success_url = reverse_lazy("reservas:reservas-list")
    success_message = "Reserva atualizada com sucesso!"

class ReservaDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = estadia
    success_url = reverse_lazy("reservas:reservas-list")