from django.conf.urls import url
from biblioApp.views import *

urlpatterns = [
    url(r'^meta/$', atributos_meta),
    url(r'^buscar/$', buscar),
    url(r'^contactos/$', contactos),
    url(r'^contactos/gracias/$', exito),
]
