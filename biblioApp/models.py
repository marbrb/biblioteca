from django.db import models

class Editor(models.Model):
    nombre = models.CharField(max_length=30)
    domicilio = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=60)
    estado = models.CharField(max_length=30)
    pais = models.CharField(max_length=50)
    website = models.URLField()

    class Meta: #clase especial para metadatos
        ordering = ["nombre"]
        verbose_name_plural = "Editores"

    def __str__(self):
        return self.nombre

class Autor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=40)
    email = models.EmailField(blank=True, verbose_name='e-mail')

    class Meta:
        verbose_name_plural = "Autores"

    def __str__(self):
        return "{} {}".format(self.nombre, self.apellido)

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autores = models.ManyToManyField(Autor)
    editor = models.ForeignKey(Editor)   #un solo editor
    fecha_publicacion = models.DateField(blank=True, null=True)
    portada = models.ImageField(upload_to='portadas',blank=True, default=None)   #apt-get install libjpeg-dev


    def __str__(self):
        return self.titulo
