from django.http import HttpResponse
from django.shortcuts import render, redirect
from travelapp.forms import ComidaForm

from .models import Comida


# Create your views here.


def index(request):
    comida = Comida.objects.all()
    return render(request, "index.html", {'comida': comida})


def detail(request, comida_id):
    comida = Comida.objects.get(id=comida_id)
    return render(request, 'detail.html', {'comida': comida})


def add_comida(request):
    if request.method == 'POST':
        nombre = request.POST.get("nombre", )
        ingredientes = request.POST.get("ingredientes", )
        precio = request.POST.get("precio")
        imagen = request.FILES["imagen"]
        comida = Comida(nombre=nombre, ingredientes=ingredientes, precio=precio, imagen=imagen)
        comida.save()
        return redirect('/')
    return render(request, 'add.html')


def update(request, id):
    comida = Comida.objects.get(id=id)
    form = ComidaForm(request.POST or None, request.FILES, instance=comida)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form': form, 'comida': comida})


def delete(request,id):
    if request.method == 'POSt':
        comida = Comida.objects.get(id=id)
        comida.delete()
        return redirect('/')
    return render(request, 'delete.html')
