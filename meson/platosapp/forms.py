from django import forms

from .models import Ingrediente, Producto


class IngredienteForm(forms.ModelForm):

    class Meta:
        model = Ingrediente
        fields = ('producto', 'cantidad',)


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

