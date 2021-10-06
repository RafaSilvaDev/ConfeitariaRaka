from home.models import Bolo
from django.db.models import Q
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
def index(request):
    dados = Bolo.objects.order_by('sabor').filter(
        mostrar = True
    )
    return render(request, 'home/index.html', {'dados':dados})

def mostrar(request, idbusca):
    dados = Bolo.objects.get(id=idbusca)
    return render(request, 'home/detbolo.html',{'dados': dados})

def buscar(request):
    x = request.GET['buscar'] 

    if x is None or not x:
        messages.add_message(request,messages.INFO, 'Digite um valor valido')
        redirect('home')
        
    dados = Bolo.objects.order_by('sabor').filter(
        Q(sabor__icontains = x) | Q(descricao__icontains = x)# | ou
    )
    return render(request,'home/index.html',{'dados':dados})
