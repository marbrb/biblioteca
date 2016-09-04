from random import choice

phrases = ["Django is great", "Hackers cristianos :v", "Hack the world"]

#un procesador de contexto permite agregar datos alcontexto que usan las plantillas para renderizarse
#por tanto, debe retornar un dict
def randomPhrase(request):
    return {"phrase" : choice(phrases)}
