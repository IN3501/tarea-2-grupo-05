from django.urls import path
from .views import * 

urlpatterns = [
	path('', index, name ='index'),
	path('registro', registro, name='registro'),	
	path('recuperar', recuperar, name='recuperar'),
	path('recuperar2', recuperar2, name='recuperar2'),
	path('inicio_sesion', inicio_sesion, name='inicio_sesion'),
	path('cotizacion', cotizacion, name='cotizacion'),
	path('contacto', contacto, name='contacto')	
]