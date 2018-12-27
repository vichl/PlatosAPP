from django.urls import path

from . import views


app_name = 'platosapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('plato/<int:plato_id>/', views.plato, name='plato'),
    path('plato/<int:plato_id>/ingredienteNuevo/', views.nuevo_ingrediente, name='nuevo_ingrediente'),
]
