from django.conf.urls import url
from biblioApp.views import *

urlpatterns = [
    url(r'^meta/$', atributos_meta),
    url(r'^formulario-buscar/$', form_buscar),
    url(r'^buscar/$', buscar)
]
