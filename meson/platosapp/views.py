from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Familia, Plato, Producto, Ingrediente, Categoria
from .forms import IngredienteForm


# Create your views here.

def index(request):
    categorias_lista = Categoria.objects.order_by('nombre')
    categorias = []
    for cat in categorias_lista:
        categorias.append({'nombre': cat.nombre, 'platos': Plato.objects.filter(categoria=cat.id).order_by('nombre')})
    context = {
        'categorias': categorias,
    }
    return render(request, 'platosapp/listado_platos.html', context)


def plato(request, plato_id):
    plato_obj = get_object_or_404(Plato, id=plato_id)
    # ingredientes_lista = plato_obj.ingrediente_set.all()
    ingredientes_lista = Ingrediente.objects.filter(plato=plato_id).order_by('-cantidad')
    ingredientes = []
    costeTotal = 0
    for i in ingredientes_lista:
        ingredientes.append({'nombre': i.producto.nombre,
                             'cantidad': str(i.cantidad) + i.producto.unidades,
                             'coste': str(round(i.cantidad * i.producto.precio, 2))})
        costeTotal += i.cantidad * i.producto.precio
    context = {
        'plato': plato_obj,
        'ingredientes_lista': ingredientes,
        'costeTotal': round(costeTotal, 2),
    }
    return render(request, 'platosapp/plato.html', context)


def nuevo_ingrediente(request, plato_id):
    form = IngredienteForm()
    context = {'form': form,
               'plato_id': plato_id}
    return render(request, 'platosapp/ingrediente_nuevo.html', context)




