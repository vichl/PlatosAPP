from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import Familia, Plato, Producto, Ingrediente, Categoria
from .forms import CategoriaForm, FamiliaForm, IngredienteForm, PlatoForm, ProductoForm


# CATEGORÍA
def listado_categorias(request):
    categorias_lista = Categoria.objects.order_by('nombre')
    context = {
        'categorias': categorias_lista,
    }
    return render(request, 'platosapp/listado_categorias.html', context)

def nueva_categoria(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            cat = form.save(commit=False)
            cat.save()
            return HttpResponseRedirect('/categoria/listado')
    else:
        form = CategoriaForm()
        context = {
            'form': form,
        }
        return render(request, 'platosapp/categoria.html', context)

def editar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    if request.method == "POST":
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            cat = form.save(commit=False)
            cat.id = categoria_id
            cat.save()
            return HttpResponseRedirect('/categoria/' + str(categoria_id))
       
    else:
        form = CategoriaForm(instance=categoria)
    context = {
        'form': form,
        'categoria': categoria,
    }
    return render(request, 'platosapp/categoria.html', context)

def borrar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    categoria.delete()
    return HttpResponseRedirect('/categoria/listado')


# PLATOS
def listado_platos(request):
    categorias_lista = Categoria.objects.order_by('nombre')
    categorias = []
    for cat in categorias_lista:
        categorias.append({'nombre': cat.nombre, 'platos': Plato.objects.filter(categoria=cat.id).order_by('nombre')})
    context = {
        'categorias': categorias,
    }
    return render(request, 'platosapp/listado_platos.html', context)

def nuevo_plato(request):
    if request.method == "POST":
        form = PlatoForm(request.POST)
        if form.is_valid():
            pla = form.save(commit=False)
            pla.save()
            return HttpResponseRedirect('/plato/listado')
    else:
        form = PlatoForm()
        context = {
            'form': form,
        }
        return render(request, 'platosapp/plato.html', context)   

def editar_plato(request, plato_id):
    plato = get_object_or_404(Plato, id=plato_id)
    if request == 'POST':
        form = PlatoForm(request.POST, instance=plato)
        if form.is_valid():
            pla = form.save(commit=False)
            pla.id = plato_id
            pla.save()
            return HttpResponseRedirect('/plato/' + str(plato_id))
    else: 
        familias_lista = Familia.objects.all().order_by('nombre')
        ingredientes_lista = Ingrediente.objects.filter(plato=plato_id).order_by('-cantidad')
        ingredientes = []
        costeTotal = 0
        for i in ingredientes_lista:
            ingredientes.append({'id': i.id,
                                'nombre': i.producto.nombre,
                                'cantidad': str(i.cantidad) + i.producto.unidades,
                                'coste': str(round(i.cantidad * i.producto.precio, 2))})
            costeTotal += i.cantidad * i.producto.precio
        form = PlatoForm(instance=plato)
        context = {
            'plato': plato,
            'ingredientes_lista': ingredientes,
            'costeTotal': round(costeTotal, 2),
            'familias_lista': familias_lista,
            'form': form,
        }
        return render(request, 'platosapp/plato.html', context)

def borrar_plato(request, plato_id):
    pla = get_object_or_404(Plato, id=plato_id)
    pla.delete()
    return HttpResponseRedirect('/plato/listado')

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


# FAMILIA
def listado_familias(request):
    familias = Familia.objects.all().order_by('nombre')
    context = {
        'familias': familias,
    }
    return render(request, 'platosapp/listado_familias.html', context)

def nueva_familia(request):
    if request.method == "POST":
        form = FamiliaForm(request.POST)
        if form.is_valid():
            fam = form.save(commit=False)
            fam.save()
            return HttpResponseRedirect('/familia/listado')
    else:
        form = FamiliaForm()
        context = {
            'form': form,
        }
        return render(request, 'platosapp/familia.html', context)

def editar_familia(request, familia_id):
    familia = get_object_or_404(Familia, id=familia_id)
    if request.method == "POST":
        form = FamiliaForm(request.POST, instance=familia)
        if form.is_valid():
            fam = form.save(commit=False)
            fam.id = familia_id
            fam.save()
            return HttpResponseRedirect('/familia/' + str(familia_id))
       
    else:
        form = FamiliaForm(instance=familia)
    context = {
        'form': form,
        'familia': familia,
    }
    return render(request, 'platosapp/familia.html', context)

def borrar_familia(request, familia_id):
    familia = get_object_or_404(Familia, id=familia_id)
    familia.delete()
    return HttpResponseRedirect('/familia/listado')

# PRODUCTO
def listado_productos(request):
    familias_lista = Familia.objects.all().order_by('nombre')
    familias = []
    for fam in familias_lista:
        familias.append({'nombre': fam.nombre, 'productos': Producto.objects.filter(familia=fam.id).order_by('nombre')})
    context = {
        'familias': familias,
    }
    return render(request, 'platosapp/listado_productos.html', context)

def nuevo_producto(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            prod = form.save(commit=False)
            prod.save()
            return HttpResponseRedirect('/producto/listado')
    else:
        form = ProductoForm()
        context = {
            'form': form,
        }
        return render(request, 'platosapp/producto.html', context)

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

def borrar_producto(request, producto_id): 
    producto = get_object_or_404(Producto, id=producto_id)
    producto.delete()
    return HttpResponseRedirect('/producto/listado')

def ajax_productos(request):
    familia_id = request.GET.get('familiaId')
    productos = Producto.objects.filter(familia=familia_id).order_by('nombre')

    return render(request, 'platosapp/select_dependiente.html', {'opciones': productos})
