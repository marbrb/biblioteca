
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from biblioApp.models import Libro
from django.core.mail import send_mail
from biblioApp.forms import FormularioContactos


def atributos_meta(request):
    valor = request.META.items()    #return a list of tuples.
    return render_to_response('meta.html', {'path':request.path,'secure':request.is_secure(),'lista':valor})

def buscar(request):
    #request.GET/POST es un diccionario que permite el acceso a datos(get/post)
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Por favor introduce un término de búsqueda.')
        elif len(q) > 20:
            errors.append('Por favor introduce un término de búsqueda menor a 20 caracteres.')
        else:
            libros = Libro.objects.filter(titulo__icontains=q)  #todos los libros que incluyan en el titulo lo que tenga q
            return render_to_response('resultados.html', {'libros':libros,'query':q})

    return render_to_response('search_form.html', {'errors':errors})

def exito(request):
    return render_to_response('exito.html')


def contactos(request):
    if request.method == 'POST':
        #request.GET/POST es un diccionario que permite el acceso a datos(get/post)
        form = FormularioContactos(request.POST)
        if form.is_valid():
            cd = form.cleaned_data #diccionario de datos enviados 'Limpiamente'
            send_mail(
                cd['asunto'],
                cd['mensaje'],
                cd.get('email', 'noremply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contactos/gracias/')
    else:
        form = FormularioContactos()
    return render(request, 'contactos.html', {'form':form})
