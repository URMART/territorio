from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Mensajes tipo cookie temporales
from django.contrib import messages

#Gestión de Errores de base de datos
from django.db import IntegrityError

#Para paginado
from django.core.paginator import Paginator


from .models import *

# Create your views here.

def inicio(request):
    #return HttpResponse(request, 'territorium/index.html')

    return render(request,'territorium/index.html')


def aprendices(request):
    q = Aprendiz.objects.all()
    
    pag = Paginator(q, 4)   #cinco registros por página
    page_number = request.GET.get('page')
    
    #sobreescribo el query
    q = pag.get_page(page_number)
    
    contexto = {'page_obj': q}

    return render(request,'territorium/aprendices/listar_aprendiz.html',contexto)

def aprendicesBuscar(request):
    if request.method == "POST":
        
        from django.db.models import Q
        
        q = Aprendiz.objects.filter(
            Q(nombre__icontains = request.POST["dato"]) | 
            Q(apellido__icontains = request.POST["dato"]) | 
            Q(cedula__icontains = request.POST["dato"])
        )
        
        pag = Paginator(q, 4)   #cinco registros por página
        page_number = request.GET.get('page')
        
        #sobreescribo el query
        q = pag.get_page(page_number)
        
        contexto = {'page_obj': q, "dato_buscado": request.POST["dato"]}

        return render(request,'territorium/aprendices/listar_aprendiz_ajax.html',contexto)
    else:
        messages.warning(request, "Usted no envió datos...")
        return redirect('territorium:aprendices')

def aprendicesFormulario(request):
    return render(request, 'territorium/aprendices/crear_aprendiz.html') 

def aprendicesGuardar(request):
    try:
        if request.method == "POST":
            q = Aprendiz(
                cedula = request.POST["cedula"],
                nombre = request.POST["nombre"],
                apellido = request.POST["apellido"],
                fecha_nacimiento = request.POST["fecha_nacimiento"],
            )
            q.save()
            
            messages.success(request, "Aprendiz guardado correctemente!")
            return redirect('territorium:aprendices')
        else:
            messages.warning(request, "Usted no envió datos...")
            return redirect('territorium:aprendices')
    except Exception as e:
        messages.error(request, "Error: " + str(e))
        return redirect('territorium:aprendices')
        

def aprendicesEliminar(request,id):
    try:
        a = Aprendiz.objects.get(pk = id)
        a.delete()
        return HttpResponseRedirect(reverse('territorium:aprendices'))
    except Aprendiz.DoesNotExist:
        return HttpResponse('ERROR: Aprendiz no existe')
    except Exception as e:
        return HttpResponse(f'error: {e}')


def aprendizFormularioEditar(request, id):
    a = Aprendiz.objects.get(pk = id)
    contexto = { "datos": a }
    
    return render(request, 'territorium/aprendices/editar_aprendiz.html', contexto)


def actualizarAprendiz(request):
    try:
        if request.method == "POST":
            a = Aprendiz.objects.get(pk = request.POST["id"])
            
            a.cedula = request.POST["cedula"]
            a.nombre = request.POST["nombre"]
            a.apellido = request.POST["apellido"]
            a.fecha_nacimiento = request.POST["fecha_nacimiento"]
            
            a.save()
            
            messages.success(request, "Aprendiz actualizado correctemente!")
            return redirect('territorium:aprendices')
        else:
            messages.warning(request, "Usted no envió datos...")
            return redirect('territorium:aprendices')
    except Exception as e:
        messages.error(request, "Error: " + str(e))
        return redirect('territorium:aprendices')
     

def monitorias(request):
    q = Monitoria.objects.all()
    contexto = {'datos': q}
    return render(request,'territorium/monitorias/listar_monitorias.html',contexto)

def monitoriasFormulario(request):
    q = Aprendiz.objects.all()
    contexto = {'datos':q}
    return render(request, 'territorium/monitorias/crear_monitorias.html',contexto) 

def monitoriasGuardar(request):
    
    try:
        a = Aprendiz.objects.get(pk = request.POST["aprendiz"])
        
        q = Monitoria(
            cat = request.POST["cat"],
            aprendiz = a,
            fecha_inicio = request.POST["fecha_inicio"],
            fecha_final = request.POST["fecha_final"],
        )
        q.save()
        #return HttpResponse("Monitoria guardada correctemente! <br/> <a href='../monitorias/'>Listar Monitorias</a> ")
        return HttpResponseRedirect(reverse('territorium:monitorias'))
    except Exception as e:
         return HttpResponse("Error: " + str(e))
    
def monitoriasEliminar(request,id):
    try:
        a = Monitoria.objects.get(pk = id)
        a.delete()
        return HttpResponseRedirect(reverse('territorium:monitorias'))
    except Aprendiz.DoesNotExist:
        return HttpResponse('ERROR: Monitoria no existe')
    except Exception as e:
        return HttpResponse(f'error: {e}')

def actividades(request):
    q = Actividades.objects.all()
    contexto = {'datos': q}
    return render(request,'territorium/actividades/listar_actividades.html',contexto)


def actividadesFormulario(request):
    q = Monitoria.objects.all()
    contexto = {'datos':q}
    return render(request, 'territorium/actividades/crear_actividades.html',contexto) 


def actividadesGuardar(request):
    
    try:
        a = Monitoria.objects.get(pk = request.POST["monitoria"])
        
        q = Actividades(
            monitoria = a,
            actividad = request.POST["actividad"],
            observaciones = request.POST["observaciones"],
            fecha = request.POST["fecha"],
        )
        q.save()
        return HttpResponseRedirect(reverse('territorium:actividades'))
    except Exception as e:
         return HttpResponse("Error: " + str(e))

def actividadesEliminar(request,id):
    try:
        a = Actividades.objects.get(pk = id)
        a.delete()
        return HttpResponseRedirect(reverse('territorium:actividades'))
    except Aprendiz.DoesNotExist:
        return HttpResponse('ERROR: Actividad no existe')
    except Exception as e:
        return HttpResponse(f'error: {e}')
    
def loginForm(request):
    
    return render(request,'territorium/login/login.html')    

def login (request):
    if request.method == 'POST':
        try:
            u=request.POST['user']
            p=request.POST['pass']
            
            q=Usuario.objects.get(usuario=u,password=p)
            
            messages.success(request, "Bienvenido")
            return redirect('territorium:loginForm') 
          
        except Usuario.DoesNotExist:
            messages.error(request, "Usuario o contraseña incorrecta") 
            return redirect('territorium:loginForm')  
    else:
            messages.warning(request, "Usted no envió datos...")
            return redirect('territorium:loginForm')  
def logout(request):
    pass
