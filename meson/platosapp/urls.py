from django.urls import path

from . import views


app_name = 'platosapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('plato/', views.index, name='listado_platos'),
    path('plato/<int:plato_id>/', views.plato, name='plato'),
    path('plato/<int:plato_id>/ingredienteNuevo/', views.nuevo_ingrediente, name='nuevo_ingrediente'),
    path('plato/<int:plato_id>/eliminarIngrediente/<int:ingrediente_id>/', views.eliminar_ingrediente, name='eliminar_ingrediente'),
    path('ajax/productos', views.ajax_productos, name='ajax_productos'),
    path('producto/', views.listado_productos, name='listado_productos'),
    path('producto/<int:producto_id>/', views.editar_producto, name='producto'),
    path('producto/nuevo', views.nuevo_producto, name='nuevo_producto'),
]
