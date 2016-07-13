from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from biblioApp.models import Libro
from django.core.mail import send_mail


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

#esto debería ir en una nueva app?
def contactos(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('asunto', ''):
            errors.append('Por favor introduce el asunto.')
        elif not request.POST.get('mensaje', ''):
            errors.append('Por favor introduce un mensaje.')
        elif request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Por favor introduce una direccion de e­mail valida.')
        if not errors:
            send_mail(
                request.POST['asunto'],
                request.POST['mensaje'],
                request.POST.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )

            return HttpResponseRedirect('/contactos/gracias/')

    return render_to_response(
        'contactos.html',
         {'errors': errors,
         'asunto': request.POST.get('asunto', ''),
         'mensaje': request.POST.get('mensaje', ''),
         'email': request.POST.get('email', ''),}
    )
