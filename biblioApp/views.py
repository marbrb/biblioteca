from django.shortcuts import render_to_response
from django.http import HttpResponse
from biblioApp.models import Libro

def atributos_meta(request):
    valor = request.META.items()    #return a list of tuples.
    return render_to_response('meta.html', {'path':request.path,'secure':request.is_secure(),'lista':valor})

def form_buscar(request):
    return render_to_response('search_form.html')

def buscar(request):
    #request.GET/POST es un diccionario que permite el acceso a datos(get/post)
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        libros = Libro.objects.filter(titulo__icontains=q)  #todos los libros que incluyan en el titulo lo que tenga q
        return render_to_response('resultados.html', {'libros':libros,'query':q})
    else:
        return HttpResponse("Por favor introduce un termino de búsqueda.")
