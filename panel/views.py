from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from web_sabores.models import Consulta
from panel.models import  UsuarioPermitido
import uuid

def registro(request):
    if request.method == 'POST':
        nombre   = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        email    = request.POST.get('email')
        password = request.POST.get('password')

        print(f"Email ingresado: '{email}'")

        try:
            permitido = UsuarioPermitido.objects.get(email=email)
            print(f"Usuario encontrado: {permitido}")  # ← y esto
        except UsuarioPermitido.DoesNotExist:
            print("Usuario NO encontrado")  # ← y esto
            messages.error(request, 'Acceso restringido. No está autorizado a utilizar este sistema.')
            return render(request, 'panel/registro.html')

        if User.objects.filter(username=email).exists():
            messages.error(request, 'Ya existe una cuenta con ese correo.')
            return render(request, 'panel/registro.html')

        user = User.objects.create_user(
            username=email,
            email=email,
            password=password,
            first_name=nombre,
            last_name=apellido,
            is_active=False
        )

        try:
            send_mail(
                subject='Validá tu cuenta — Sabores del Mundo',
                message=f'''Hola {nombre},

Tu código de validación es: {permitido.codigo_validacion}

Ingresá al siguiente enlace para validar tu cuenta:
http://127.0.0.1:8000/panel/validar/

Ingresá tu email y el código para activar tu cuenta.

Saludos,
Sabores del Mundo''',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[email],
                fail_silently=True,
            )
        except:
            pass

        messages.success(request, 'Le llegará un correo para validar su cuenta.')
        return redirect('validar')

    return render(request, 'panel/registro.html')


def validar(request):
    if request.method == 'POST':
        email  = request.POST.get('email')
        codigo = request.POST.get('codigo')

        try:
            permitido = UsuarioPermitido.objects.get(email=email, codigo_validacion=codigo)
            user = User.objects.get(username=email)
            user.is_active = True
            user.save()
            messages.success(request, '¡Cuenta validada! Ya podés iniciar sesión.')
            return redirect('login_panel')
        except:
            messages.error(request, 'Código o email incorrecto.')

    return render(request, 'panel/validar.html')


def login_panel(request):
    if request.method == 'POST':
        email    = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Email o contraseña incorrectos.')

    return render(request, 'panel/login.html')


def logout_panel(request):
    logout(request)
    return redirect('login_panel')


@login_required(login_url='/panel/login/')
def dashboard(request):
    consultas = Consulta.objects.all()
    total = consultas.count()

    stats = {
        'Consulta Comercial': consultas.filter(categoria='Consulta Comercial').count(),
        'Consulta Técnica':   consultas.filter(categoria='Consulta Técnica').count(),
        'Consulta de RRHH':   consultas.filter(categoria='Consulta de RRHH').count(),
        'Consulta General':   consultas.filter(categoria='Consulta General').count(),
    }

    return render(request, 'panel/dashboard.html', {
        'consultas': consultas,
        'total': total,
        'stats': stats,
    })


@login_required(login_url='/panel/login/')
def eliminar_consulta(request, id):
    try:
        consulta = Consulta.objects.get(id=id)
        consulta.delete()
        messages.success(request, 'Consulta eliminada.')
    except:
        messages.error(request, 'No se encontró la consulta.')
    return redirect('dashboard')