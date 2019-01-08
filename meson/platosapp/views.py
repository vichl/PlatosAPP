from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import Familia, Plato, Producto, Ingrediente, Categoria
from .forms import IngredienteForm, ProductoForm


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

def listado_productos(request):
    familias_lista = Familia.objects.all().order_by('nombre')
    familias = []
    for fam in familias_lista:
        familias.append({'nombre': fam.nombre, 'productos': Producto.objects.filter(familia=fam.id).order_by('nombre')})
    context = {
        'familias': familias,
    }
    return render(request, 'platosapp/listado_productos.html', context)


def plato(request, plato_id):
    plato_obj = get_object_or_404(Plato, id=plato_id)
    # ingredientes_lista = plato_obj.ingrediente_set.all()
    familias_lista = Familia.objects.all().order_by('nombre');
    ingredientes_lista = Ingrediente.objects.filter(plato=plato_id).order_by('-cantidad')
    ingredientes = []
    costeTotal = 0
    for i in ingredientes_lista:
        ingredientes.append({'id': i.id,
                             'nombre': i.producto.nombre,
                             'cantidad': str(i.cantidad) + i.producto.unidades,
                             'coste': str(round(i.cantidad * i.producto.precio, 2))})
        costeTotal += i.cantidad * i.producto.precio
    context = {
        'plato': plato_obj,
        'ingredientes_lista': ingredientes,
        'costeTotal': round(costeTotal, 2),
        'familias_lista': familias_lista,
    }
    return render(request, 'platosapp/plato.html', context)


def ajax_productos(request):
    familia_id = request.GET.get('familiaId')
    productos = Producto.objects.filter(familia=familia_id).order_by('nombre')

    return render(request, 'platosapp/select_dependiente.html', {'opciones': productos})


def nuevo_ingrediente(request, plato_id):
    if request.method == 'POST':
        form = IngredienteForm(request.POST)
        if form.is_valid():
            ing = form.save(commit=False)
            ing.plato = Plato.objects.get(id=plato_id)
            ing.save()
        '''
        plato_ing = Plato.objects.get(id=plato_id)
        producto_ing = Producto.objects.get(id=request.POST.get('producto'))
        cantidad_ing = request.POST.get('cantidad')
        Ingrediente.objects.create(producto=producto_ing, plato=plato_ing, cantidad=cantidad_ing)
        '''
    return HttpResponseRedirect('/plato/' + str(plato_id))


def eliminar_ingrediente(request, plato_id, ingrediente_id):
    if request.method == 'POST':
        Ingrediente.objects.get(id=ingrediente_id).delete()

    return HttpResponseRedirect('/plato/' + str(plato_id))


def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == "POST":
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            prod = form.save(commit=False)
            prod.id = producto_id
            prod.save()
            return HttpResponseRedirect('/producto/' + str(producto_id))
    else:
        form = ProductoForm(instance=producto)
    context = {
        'form': form,
        'producto': producto,
    }
    return render(request, 'platosapp/producto.html', context)


def nuevo_producto(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            prod = form.save(commit=False)
            prod.save()
            return HttpResponseRedirect('/producto/')
    else:
        form = ProductoForm()
    context = {
        'form': form,
    }
    return render(request, 'platosapp/producto.html', context)





