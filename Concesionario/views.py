from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render,redirect
from Concesionario.models import Auto

def listadoempleado(request):
    paginalistado = open('Concesionario/Templates/Auto/listado.html')
    lectura = Template(paginalistado.read())
    paginalistado.close()
    empleado = Auto.objects.all()
    parametros = Context({'empleado':empleado})
    paginafinal = lectura.render(parametros)
    return HttpResponse(paginafinal)

def insertarempleado(request):
    if request.method == "POST":
     if request.POST.get('cilindraje') and request.POST.get('matricula') and request.POST.get('marca') and request.POST.get('modelo') and request.POST.get('color') and request.POST.get('cojineria'):
        empleado = Auto()
        empleado.Cilindraje = request.POST.get('cilindraje')
        empleado.Matricula = request.POST.get('matricula')
        empleado.Marca = request.POST.get('marca')
        empleado.Modelo= request.POST.get('modelo')
        empleado.Color= request.POST.get('color')
        empleado.Cojineria= request.POST.get('cojineria')
        empleado.save()
        return redirect('/Auto/listado')
    else:
        return render(request,'Auto/insertar.html')


def borrarempleado(request,idempleado):
    empleado = Auto.objects.get(id=idempleado)
    empleado.delete()
    return redirect('/Auto/listado')



def actualizarempleado(request,idempleado):
    if request.method == "POST":
     if request.POST.get('cilindraje') and request.POST.get('matricula') and request.POST.get('marca') and request.POST.get('modelo') and request.POST.get('color') and request.POST.get('cojineria'):
        empleado = Auto.objects.get(id=idempleado)
        empleado.Cilindraje = request.POST.get('cilindraje')
        empleado.Matricula = request.POST.get('matricula')
        empleado.Marca = request.POST.get('marca')
        empleado.Modelo= request.POST.get('modelo')
        empleado.Color = request.POST.get('color')
        empleado.Cojineria= request.POST.get('cojineria')
        empleado.save()
        return redirect('/Auto/listado')
    else:
        empleado = Auto.objects.filter(id=idempleado)
        return render(request,'Auto/actualizar.html',{'empleado':empleado})

  