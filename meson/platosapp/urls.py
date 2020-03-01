from django.urls import path

from . import views


app_name = 'platosapp'
urlpatterns = [
    path('', views.listado_platos, name='index'),

    path('categoria/listado/', views.listado_categorias, name='listado_categorias'),
    path('categoria/nuevo/', views.nueva_categoria, name='nueva_categoria'), 
    path('categoria/<int:categoria_id>/', views.editar_categoria, name='categoria'),
    path('categoria/<int:categoria_id>/borrar/', views.borrar_categoria, name='borrar_categoria'),
    
    path('plato/listado/', views.listado_platos, name='listado_platos'),
    path('plato/nuevo/', views.nuevo_plato, name='nuevo_plato'),
    path('plato/<int:plato_id>/', views.editar_plato, name='plato'),
    path('plato/<int:plato_id>/borrar', views.borrar_plato, name='borrar_plato'),
    path('plato/<int:plato_id>/ingredienteNuevo/', views.nuevo_ingrediente, name='nuevo_ingrediente'),
    path('plato/<int:plato_id>/eliminarIngrediente/<int:ingrediente_id>/', views.eliminar_ingrediente, name='eliminar_ingrediente'),

    path('familia/listado/', views.listado_familias, name='listado_familias'),
    path('familia/nuevo/', views.nueva_familia, name='nueva_familia'),
    path('familia/<int:familia_id>/', views.editar_familia, name='familia'),
    path('familia/<int:familia_id>/borrar/', views.borrar_familia, name='borrar_familia'),

    path('producto/listado/', views.listado_productos, name='listado_productos'),
    path('producto/nuevo/', views.nuevo_producto, name='nuevo_producto'),
    path('producto/<int:producto_id>/', views.editar_producto, name='producto'),
    path('producto/<int:producto_id>/borrar/', views.borrar_producto, name='borrar_producto'),
    path('ajax/productos', views.ajax_productos, name='ajax_productos'),
]
