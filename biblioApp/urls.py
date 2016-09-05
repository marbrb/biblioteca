from django.conf.urls import url
from biblioApp.views import *

urlpatterns = [
    url(r'^meta/$', atributos_meta, name="meta"),
    url(r'^buscar/$', buscar, name="buscar"),
    url(r'^contactos/$', contactos, name="contactos"),
    url(r'^contactos/gracias/$', exito, name="gracias"),
]
