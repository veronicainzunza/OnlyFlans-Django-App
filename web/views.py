from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Flan, ContactForm
from .forms import ContactFormForm, ContactFormModelForm, FlanForm

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.http import Http404
from django.urls import reverse_lazy





# Create your views here.
def index(request):
    flanes_publicos = Flan.objects.filter(is_private=False)
    return render(request, 'index.html', {'flanes': flanes_publicos})


def about(request):
    return render(request, 'about.html')

@login_required
def welcome(request):
    flanes_privados = Flan.objects.filter(is_private=True)
    return render(request, 'welcome.html', {'flanes': flanes_privados})

def contacto(request):
    if request.method == 'POST':
        form = ContactFormForm(request.POST)
        if form.is_valid():

            # Crear un nuevo registro basado en los datos del formulario
            #ContactForm.objects.create(
            #    customer_email=form.cleaned_data['customer_email'],
            #    customer_name=form.cleaned_data['customer_name'],
            #    message=form.cleaned_data['message'])

            # Procesar datos en form.cleaned_data
            ContactForm.objects.create(**form.cleaned_data)
            
            return redirect('registro_exitoso')  # Redirigir a una página de éxito
    else:
        form = ContactFormForm()
    return render(request, 'contacto.html', {'form': form})


def contacto_model(request):
    if  request.method == 'POST':
        # Construir instancia del formulario con parametros en el cuerpo de la request
        form = ContactFormModelForm(request.POST)
        # Validar formulario
        if form.is_valid():

            form.save()
            # Redireccionar a nueva url
            return redirect('registro_exitoso')  # Redirigir a una página de éxito
    else:
        form = ContactFormModelForm()

    return render(request,'contact.html', {'form' : form})  

def registro_exitoso(request):
    return render(request, 'registro_exitoso.html')


def map_view(request):
    return render(request, 'map.html')

def detalle_flan(request, flan_id):
    flan = get_object_or_404(Flan, id=flan_id)
    return render(request, 'detalle.html', {'flan': flan})

#class FlanCreateView(CreateView):
#    model = Flan
#    template_name = "agregar_flan.html"
#    fields = ['flan_uuid', 'name', 'description', 'image_url', 'slug','is_private']
#    success_url = reverse_lazy('index')-->

class FlanCreateView(CreateView):
    model = Flan
    form_class = FlanForm
    template_name = "agregar_flan.html"
    success_url = reverse_lazy('index')


    



 









    







