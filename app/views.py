from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .models import Miembro
import pytz 

# Create your views here.

def home(request):
    return render(request, 'home.html')

@login_required
def actuser(request):
    tz = pytz.all_timezones
    # Verificar si el usuario ya tiene un Miembro asociado
    try:
        extuser = Miembro.objects.filter(user=request.user).count()
        datuser = Miembro.objects.get(user=request.user)
    except Miembro.DoesNotExist:
        datuser = None

    if request.method == 'POST':
        if 'mostrarnombre' in request.POST:
                mostrarn = True
        else:
                mostrarn = False
        # Actualizar el perfil del usuario y crear un Miembro si no existe
        if extuser > 0:
            # Actualizar el Miembro existente
            datuser.gametag = request.POST['gametag']
            datuser.pais = request.POST['pais']
            datuser.zonah = request.POST['zona_horaria']
            datuser.horai = request.POST['hora']
            datuser.duracion = request.POST['duracion']
            datuser.mostrarnombre = mostrarn
            datuser.save()
        else:
            # Crear un nuevo Miembro
            Miembro.objects.create(
                user=request.user,
                gametag=request.POST['gametag'],
                pais = request.POST['pais'],
                zonah = request.POST['zona_horaria'],
                horai = request.POST['hora'],
                duracion = request.POST['duracion'],
                mostrarnombre = mostrarn,
            )
        
        # Actualizar el nombre y apellido del usuario en el modelo User
        request.user.first_name = request.POST['nombre']
        request.user.last_name = request.POST['apellido']
        request.user.email = request.POST['email']
        request.user.save()
        messages.success(request, 'Informacion actualizada corretamente!!')
        return render(request, 'actuser.html', {'datuser': datuser, 'tz': tz})

    return render(request, 'actuser.html', {'datuser': datuser, 'tz': tz})
    
def loginuser(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else :
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            messages.success(request, 'El usuario o contraseña es incorrecto...')
            return render(request, 'login.html')
        else :
            login(request, user)
            return render(request, 'home.html')

def adduser(request):
    if request.method == 'GET':
        return render(request, 'altauser.html')
    else :
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'], email=request.POST['email'])
                user.save()
                login(request, user)
                messages.success(request, '¡Usuario Dado de alta!')
                return render(request, 'home.html')
            except IntegrityError:
                messages.success(request, '!Usuario ya existe¡')
                return render(request, 'altauser.html')
        else :
            messages.success(request, 'Password no son iguales')
            return render(request, 'altauser.html') 
               
@login_required
def horarios(request):
    miembros = Miembro.objects.all()
    return render(request, 'horarios.html',{
        'miembros': miembros
    })

@login_required        
def logoutuser(request):
    logout(request)
    return render(request, 'home.html   ')