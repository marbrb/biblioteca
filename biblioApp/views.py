from django.shortcuts import render_to_response

def atributos_meta(request):
    valor = request.META.items()    #return a list of tuples.

    return render_to_response('meta.html', {'path':request.path,'secure':request.is_secure(),'lista':valor})
