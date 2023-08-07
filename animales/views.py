from django.shortcuts import render, get_object_or_404, redirect
from .models import Animal
from .forms import AnimalForm
# Create your views here.

def inicio(request):
    animales = Animal.objects.all() #devuelve todo en una lista
    context = {
        'animales' : animales
    }
    return render(request,'animales/inicio.html',context)

def detail(request,id):
    detail_animal = get_object_or_404(Animal, id = id)
    context = {
        'detail_animal' : detail_animal
    }
    return render(request,'animales/detail.html',context)

def create_animal(request):
    if request.method == 'POST':
        animal_form = AnimalForm(request.POST)
        if animal_form.is_valid():
            animal_form.save();
            return redirect('aplication:inicio')
    else:
        animal_form = AnimalForm()
    return render(request,'animales/create.html',{'animal_form':animal_form})

def edit_animal(request, id):
    animal = get_object_or_404(Animal,id=id)
    if request.method == 'POST':
        animal_form = AnimalForm(request.POST,instance= animal)
        if animal_form.is_valid():
            animal_form.save();
            return redirect('aplication:inicio')
    else:
        animal_form = AnimalForm()
    return render(request,'animales/editar.html',{'animal_form':animal_form})

def delete_animal(request,id):
    animal = get_object_or_404(Animal,id=id)
    if animal:
        animal.delete()
        return redirect('aplication:inicio')