from django import forms

from .models import Categoria, Familia, Ingrediente, Plato, Producto

class CategoriaForm(forms.ModelForm):
    
    class Meta:
        model = Categoria
        fields = ('nombre',)

    def __init__(self, *args, **kwargs):
        super(CategoriaForm, self).__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs.update({'class': 'form-control'})

class FamiliaForm(forms.ModelForm):

    class Meta:
        model = Familia
        fields = ('nombre', 'observaciones')

    def __init__(self, *args, **kwargs):
        super(FamiliaForm, self).__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs.update({'class': 'form-control'})
        self.fields['observaciones'].widget.attrs.update({'class': 'form-control'})

class IngredienteForm(forms.ModelForm):

    class Meta:
        model = Ingrediente
        fields = ('producto', 'cantidad',)

class PlatoForm(forms.ModelForm):
    
    class Meta:
        model = Plato
        fields = ('nombre', 'categoria', 'precio_venta', 'observaciones')

    def __init__(self, *args, **kwargs):
        super(PlatoForm, self).__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs.update({'class': 'form-control'})
        self.fields['categoria'].widget.attrs.update({'class': 'form-control'})
        self.fields['precio_venta'].widget.attrs.update({'class': 'form-control'})
        self.fields['observaciones'].widget.attrs.update({'class': 'form-control'})
        

class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = ('nombre', 'familia', 'marca', 'proveedor', 'precio', 'unidades')

    def __init__(self, *args, **kwargs):
        super(ProductoForm, self).__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs.update({'class': 'form-control'})
        self.fields['familia'].widget.attrs.update({'class': 'form-control'})
        self.fields['marca'].widget.attrs.update({'class': 'form-control'})
        self.fields['proveedor'].widget.attrs.update({'class': 'form-control'})
        self.fields['precio'].widget.attrs.update({'class': 'form-control'})
        self.fields['unidades'].widget.attrs.update({'class': 'form-control'})

     