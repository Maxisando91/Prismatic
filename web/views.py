from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from . import forms
from django.contrib import messages

import datetime
# Create your views here.



def index(request):
    cards = [
        {
            'imagen': 'web/img/index/Artista 1.jpg',
            'titulo': 'Artista 1',
            'descripcion': 'Cras a elit non odio tempor feugiat. Integer elementum dolor eget mauris venenatis, nec sollicitudin justo posuere. Curabitur lobortis, lectus non tincidunt eleifend, purus sem sollicitudin metus, at fermentum lacus dolor in nulla. Ut laoreet sapien in felis vehicula, nec eleifend lectus tincidunt',
            'enlace': 'Artista1.html',
        },
        {
            'imagen': 'web/img/index/Artista 2.jpg',
            'titulo': 'Artista 2',
            'descripcion': 'Curabitur eu quam vel risus pulvinar dictum ac sit amet elit. Integer vitae odio semper, efficitur ex a, feugiat est. Vivamus vitae nisl a arcu faucibus feugiat. Sed nec ante id nisi bibendum hendrerit. Integer gravida turpis velit, eget vehicula nisi bibendum eget. Phasellus nec nisi vitae lacus tincidunt placerat',
            'enlace': 'Artista2.html',
        },
        {
            'imagen': "web/img/index/bon jovi 2.jpeg",
            'titulo': 'Bon Jovi',
            'descripcion': 'Bon Jovi es una banda estadounidense de rock formada en 1983 en Nueva Jersey por su líder y vocalista, Jon Bon Jovi. La formación actual la completan el teclista David Bryan, el batería Tico Torres, el bajista Hugh McDonald y el guitarrista Phil X. Este último sustituyó a Richie Sambora, quien abandonó la formación en 2013',
            'enlace': 'bonjovi',
        },
    ]
    videos = [
        {"src": "web/videos/index/Bon Jovi.mp4"},
        {"src": "web/videos/index/Jared Leto.mp4"},
        # Puedes agregar más videos aquí si es necesario
    ]
    
    context = {
        'cards': cards,
        'videos': videos,
    }
    return render(request, 'web/index.html', context)




def bonjovi(request):
    elementos = [
        {
        'titulo': "Slippery When Wet",
        'imagen': "web/img/bonjovi/1 Slippery When Wet.jpeg",
        'video': "https://www.youtube.com/watch?v=lDK9QqIzhwk",
        'span': "Livin' on a Prayer"},
        {
        'titulo': "New Jersey",
        'imagen': "web/img/bonjovi/2 New Jersey.jpg",
        'span': "I'll Be There for You",
        'video': "https://www.youtube.com/watch?v=mh8MIp2FOhc"},
        {
        'titulo': "Keep the Faith",
        'imagen': "web/img/bonjovi/3 Keep the Faith.jpg",
        'span': "Keep the Faith",
        'video': "https://www.youtube.com/watch?v=eZQyVUTcpM4",
        },
        {
        'titulo': "Crush",
        'imagen': "web/img/bonjovi/4 Crush.jpg",
        'span': "It's My Life",
        'video': "https://www.youtube.com/watch?v=vx2u5uUu3DE",
        },
        {
        'titulo': "These Days",
        'imagen': "web/img/bonjovi/5 These Days.jpg",
        'span': "These Days",
        'video': "https://www.youtube.com/watch?v=UCUzwEst3pE",
        },
        {
        'titulo': "Bounce",
        'imagen': "web/img/bonjovi/6 Bounce.jpg",
        'span': "Everyday",
        'video': "https://www.youtube.com/watch?v=870-_Fa5bgo",
        },
        {
        'titulo': "Lost Highway",
        'imagen': "web/img/bonjovi/7 Lost Highway.jpg",
        'span': "Lost Highway",
        'video': "https://www.youtube.com/watch?v=n0slRE1-g1Q",
        }
        ]

    return render(request, 'web/bonjovi.html', {'elementos': elementos} )  # Renderiza la plantilla bonjovi.html


def registro(request):
    contexto = {}

    if request.method == "GET":
        contexto['registro_form'] = forms.RegistroForm()
    else:  # asumo que es un POST
        form = forms.RegistroForm(request.POST)
        if form.is_valid():
            # Lógica para procesar los datos del formulario
            # form.save() o lo que necesites hacer con los datos
            messages.success(request,'Registro Aprobado')

            return redirect('index')
        else:
            contexto['registro_form'] = form

    print(request.POST)  # Esto imprimirá los datos del formulario en la consola para depuración

    return render(request, 'web/registro.html', contexto)
