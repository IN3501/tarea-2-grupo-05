from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'index.html')

def registro(request):
	return render(request, 'registro.html')

def inicio_sesion(request):
	return render(request, 'inicio_sesion.html')

def cotizacion(request):
	return render(request, 'cotizacion.html')

def contacto(request):
	return render(request, 'contacto.html')

def recuperar2(request):
	Nombre=request.POST["inputText"]
	diccionario={}
	diccionario["comentario"]=Nombre
	return render(request, "recuperar2.html", diccionario)

def recuperar(request):
	Usuario=request.POST["inputText2"]
	diccionario={}
	diccionario["comentario"]=Usuario
	return render(request, "recuperar.html", diccionario)
