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

def recuperar(request):
	Nombre=request.POST["inputText3"]
	Numero=request.POST["inputNumber"]
	rut=request.POST["inputNumber2"]
	email=request.POST["inputEmail"]
	direccion=request.POST["inputText4"]
	region=request.POST["input Select"]
	servicio=request.POST["input Select2"]
	descripcion=request.POST["textA"]
	diccionario={}
	diccionario["Nombre"]=Nombre
	diccionario["Numero"]=Numero
	diccionario["rut"]=rut
	diccionario["email"]=email
	diccionario["dirección"]=direccion
	diccionario["region"]=region
	diccionario["servicio"]=servicio
	diccionario["descripcion"]=descripcion
	return render(request, "recuperar3.html", diccionario)