from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import *
from django.contrib.auth import login,logout,authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
import os,nltk,numpy,tensorflow,tflearn,random,pickle,matplotlib as mltp
import json
import dload
from tensorflow.python.framework import ops
from .models import Persona



# Create your views here.
def inicio(request):#funcion de inicio
    if request.method =='GET':# sentencia de control if para determinar metodo get
      return render(request,'paginas/inicio.html',{'form': AuthenticationForm})  #retorna a la pagina de inicio de sesion
    else:# si no el usuario se debe logear con username y password
        user= authenticate(request, username=request.POST['username'],password=request.POST['password'])
        if user is None:# sentencia de control if para determinar si el usuario o contrasena no son correctos
            return render(request,'paginas/inicio.html',{'form': AuthenticationForm,'error':'username or password is incorrect'})#mostrar mensaje de error
        else:#si no tiene ningun problema se puede logear
            login(request, user)#logueo de usuario
            return redirect('solucion') #si cumple con los parametros se reridecciona hacia esta funcion

       

def home(request):
    return render(request,'paginas/home.html')

    
def registro(request):
    if request.method == 'GET':
        return render(request,'paginas/registro.html',{
            'form': UserCreationForm
        })
    else :
        if request.POST['password1']==request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'],
                email=request.POST['username'],
                password=request.POST['password1'])                
                user.save()
                login(request, user)
                return redirect('solucion')
            except IntegrityError:
                return render(request, 'paginas/registro.html',{
                    'form': UserCreationForm,
                    "error":'username already exists!!'
                })            
        return render(request, 'paginas/registro.html',{
            'form': UserCreationForm,
            "error":'Password do not match!'
        })
    
def cerrar(request):
    logout(request)
    return redirect('home')

@login_required(login_url="inicio")   
def solucion(request):    
    persona1= Persona.objects.filter(user=request.user)

    return render(request,'paginas/soluction.html',{'persona1':persona1})

@login_required(login_url="inicio")
def perfil(request):    
    persona1= Persona.objects.filter(user=request.user)
    return render(request,'paginas/perfil.html',{'persona1':persona1})

@login_required(login_url="inicio")
def editar_perfil(request,cc):
    if request.method == 'GET':
        persona=get_object_or_404(Persona,pk=cc)
        form=PersonaForm(request.POST or None,request.FILES or None,instance=persona)
        return render(request,'paginas/editarper.html',{'persona':persona,'form':form})
    else:
        try:
            persona=get_object_or_404(Persona,pk=cc)
            form=PersonaForm(request.POST or None,request.FILES or None,instance=persona)
            form.save()
            return redirect('perfil')
        except ValueError:
            return render(request,'paginas/editarper.html',{'perfil':persona,'form':form,'':"Error updating pepole"})
def eliminar_perfil(request,cc):
    persona=get_object_or_404(Persona,pk=cc)    
    persona.delete()
    return redirect('home')

    

@login_required(login_url="inicio")   
def usuario(request):
    if request.method == 'GET':
        return render(request,'paginas/usuario.html',{'form': PersonaForm})
    else:
        try:
            form = PersonaForm(request.POST or None,request.FILES or None)
            new_user=form.save(commit=False)
            new_user.user=request.user
            new_user.save()
            return redirect('solucion')        
            
        except ValueError:
            return render(request,'paginas/usuario.html',{'form':PersonaForm,'error':'please provide valida data'})
    

    