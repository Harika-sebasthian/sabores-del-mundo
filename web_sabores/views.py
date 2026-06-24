from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Consulta
from .forms import ConsultaForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ConsultaSerializer


PLATOS = [
    {
        'id': 1,
        'nombre': 'Salmón sobre Terciopelo de Arvejas',
        'origen': 'Francia',
        'descripcion': 'Filete de salmón dorado sobre puré sedoso de arvejas frescas, hongos salteados y brotes silvestres.',
        'imagen': 'web_sabores/img/plato1.png',
    },
    {
        'id': 2,
        'nombre': 'Pollo Miso con Zapallo Caramelizado',
        'origen': 'Japón',
        'descripcion': 'Muslo de pollo marinado en miso y jengibre, acompañado de zapallo asado con sésamo y rúcula fresca.',
        'imagen': 'web_sabores/img/plato2.png',
    },
    {
        'id': 3,
        'nombre': 'Tartar de Atún con Palta y Sésamo',
        'origen': 'Japón · Perú',
        'descripcion': 'Tartar de atún rojo con palta laminada, sésamo negro, salsa ponzu y brotes de cilantro.',
        'imagen': 'web_sabores/img/plato3.png',
    },
    {
        'id': 4,
        'nombre': 'Langostinos a la Brasa con Aioli de Azafrán',
        'origen': 'España',
        'descripcion': 'Langostinos enteros braseados con manteca de hierbas, servidos sobre aioli de azafrán y lima.',
        'imagen': 'web_sabores/img/plato4.png',
    },
    {
        'id': 5,
        'nombre': 'Salmón a la Plancha con Tomates Heirloom',
        'origen': 'Escandinavia',
        'descripcion': 'Salmón de plancha con piel crujiente, tomates heirloom asados, rúcula y reducción balsámica.',
        'imagen': 'web_sabores/img/plato5.png',
    },
    {
        'id': 6,
        'nombre': 'Pulpo Braseado con Quinoa y Merlot',
        'origen': 'Mediterráneo',
        'descripcion': 'Tentáculos de pulpo braseados sobre quinoa dorada, emulsión de vino tinto y brotes de rúcula.',
        'imagen': 'web_sabores/img/plato6.png',
    },
    {
        'id': 7,
        'nombre': 'Zapallo Rostizado con Ricotta y Granada',
        'origen': 'Medio Oriente',
        'descripcion': 'Rodajas de zapallo caramelizado con ricotta de hierbas, semillas de granada y tomillo fresco.',
        'imagen': 'web_sabores/img/plato7.png',
    },
    {
        'id': 8,
        'nombre': 'Portobello Relleno con Queso de Cabra',
        'origen': 'Italia',
        'descripcion': 'Hongos portobello rellenos de queso de cabra gratinado con tomillo fresco y aceite de oliva.',
        'imagen': 'web_sabores/img/plato8.png',
    },
    {
        'id': 9,
        'nombre': 'Pulpo a la Gallega con Aceite Verde',
        'origen': 'España',
        'descripcion': 'Rodajas de pulpo a la gallega con aceite de perejil, mayonesa de limón y pimentón ahumado.',
        'imagen': 'web_sabores/img/plato9.png',
    },
    {
        'id': 10,
        'nombre': 'Canelones de Zucchini con Ricotta',
        'origen': 'Italia',
        'descripcion': 'Láminas de zucchini grillado rellenas de ricotta, salmón ahumado y semillas de sésamo negro.',
        'imagen': 'web_sabores/img/plato10.png',
    },
    {
        'id': 11,
        'nombre': 'Lomo Sellado con Reducción de Vino',
        'origen': 'Argentina',
        'descripcion': 'Lomo sellado a fuego vivo con reducción de Malbec, tomates cherry asados y tomillo fresco.',
        'imagen': 'web_sabores/img/plato11.png',
    },
    {
        'id': 12,
        'nombre': 'Costillar de Cordero Lacado',
        'origen': 'Francia',
        'descripcion': 'Costillar de cordero lacado con miel y romero, zanahorias glaseadas, espárragos y jus de cerezas.',
        'imagen': 'web_sabores/img/plato12.png',
    },
]


def inicio(request):
    contexto = {
        'titulo': 'Inicio',
        'platos_destacados': PLATOS[:3],
        'total_platos': len(PLATOS),
    }
    return render(request, 'web_sabores/inicio.html', contexto)


def sabores(request):
    contexto = {
        'titulo': 'Nuestros Sabores',
        'platos': PLATOS,
        'total': len(PLATOS),
    }
    return render(request, 'web_sabores/sabores.html', contexto)


def contacto(request):
    form = ConsultaForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            consulta = Consulta(
                nombre  = form.cleaned_data['nombre'],
                email   = form.cleaned_data['email'],
                asunto  = form.cleaned_data['asunto'],
                mensaje = form.cleaned_data['mensaje'],
            )
            consulta.save()

            # Email al cliente
            try:
                send_mail(
                    subject=f'[{consulta.categoria}] Nueva consulta de {consulta.nombre}',
                    message=f'''Nombre: {consulta.nombre}
Email: {consulta.email}
Asunto: {consulta.asunto}
Categoría: {consulta.categoria}

Mensaje:
{consulta.mensaje}''',
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[consulta.email],
                    fail_silently=True,
                )
            except:
                pass

            messages.success(request, f'¡Gracias, {consulta.nombre}! Tu mensaje fue recibido.')
            return redirect('contacto')
        else:
            messages.error(request, 'Por favor completá todos los campos correctamente.')

    return render(request, 'web_sabores/contacto.html', {'form': form})

@api_view(['GET'])
def api_consultas(request):
    consultas = Consulta.objects.all()
    serializer = ConsultaSerializer(consultas, many=True)
    return Response(serializer.data)

import requests

def gastronomia_mundial(request):
    platos_api = []
    try:
        response = requests.get('https://www.themealdb.com/api/json/v1/1/search.php?s=')
        if response.status_code == 200:
            data = response.json()
            platos_api = data.get('meals', [])[:6]
    except:
        platos_api = []

    return render(request, 'web_sabores/gastronomia.html', {
        'platos_api': platos_api,
        'titulo': 'Gastronomía Mundial'
    })