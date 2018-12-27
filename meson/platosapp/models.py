from django.db import models


# Create your models here.
class Familia(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    observaciones = models.TextField(max_length=500, blank=True, default="")

    def __str__(self):
        return self.nombre


class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre


class Plato(models.Model):
    nombre = models.CharField(max_length=200, unique=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    observaciones = models.TextField(max_length=500, blank=True, default="")

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    familia = models.ForeignKey(Familia, on_delete=models.CASCADE)
    marca = models.CharField(max_length=100, blank=True, default="")
    proveedor = models.CharField(max_length=100, blank=True, default="")
    precio = models.FloatField(default=0)
    unidades = models.CharField(max_length=20)
    observaciones = models.TextField(max_length=500, blank=True, default="")

    def __str__(self):
        return self.nombre


class Ingrediente(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    plato = models.ForeignKey(Plato, on_delete=models.CASCADE)
    cantidad = models.FloatField(default=0)

    def __str__(self):
        return str(self.producto)



