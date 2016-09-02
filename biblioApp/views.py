from django.shortcuts import render
from django.http import HttpResponseRedirect
from biblioApp.models import Libro
from django.core.mail import send_mail
from biblioApp.forms import FormularioContactos


def atributos_meta(request):
    valor = request.META.items()    #return a list of tuples of HTTP headers
    return render(request, 'meta.html', {'path':request.path,'secure':request.is_secure(),'lista':valor})
    #path retorna la ruta cin el dominio --- is_secure retorna true si la peticion es hecho mediante HTTPS

def buscar(request):
    #request.GET/POST es un diccionario que permite el acceso a datos(get/post)
    errors = []
    if 'busqueda' in request.GET:   #verificar que tenga la clave 'busqueda'
        busqueda = request.GET['busqueda']
        if not busqueda:
            errors.append('Por favor introduce un término de búsqueda.')
        elif len(busqueda) > 20:
            errors.append('Por favor introduce un término de búsqueda menor a 20 caracteres.')
        else:
            libros = Libro.objects.filter(titulo__icontains=busqueda)  #todos los libros que incluyan en el titulo lo que tenga busqueda
            return render(request, 'resultados.html', {'libros':libros,'query':busqueda})

    return render(request, 'search_form.html', {'errors':errors})

def exito(request):
    return render(request, 'exito.html')


def contactos(request):
    if request.method == 'POST':
        #request.GET/POST es un diccionario que permite el acceso a datos(get/post)
        form = FormularioContactos(request.POST)
        if form.is_valid():
            cd = form.cleaned_data #diccionario de datosque se enviaron bien del form
            send_mail(
                cd['asunto'],
                cd['mensaje'],
                cd.get('email', 'noremply@example.com'),
                ['marbrb1@gmail.com'],
            )
            return HttpResponseRedirect('/contactos/gracias/')
    else:
        form = FormularioContactos(initial={'asunto':'¡Adoro tu sitio!'})
    return render(request, 'contactos.html', {'form':form})
