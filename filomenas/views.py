from django.contrib import messages
from django.views.generic import ListView,CreateView,DeleteView,DetailView, UpdateView,TemplateView
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.messages import views

class Index(generic.TemplateView):
    template_name = "filomenas/index.html"

