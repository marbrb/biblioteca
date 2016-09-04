from django.shortcuts import redirect
from random import choice
#Los middlewares son elementos que permiten cambiar GLOBALMENTE el comportamiento
#de la aplciacion modificando la entrada y la salida

def randomCountry():
    return choice(['Colombia', 'Mexico', 'Chile'])

class PaisMiddleware(object):
    def process_request(self, request):
        country = randomCountry()
        if country == 'Chile':
            return redirect('http://localhost:8000/buscar/')    #que flojera hacer una vista para chile


    #Tambien esta process response
