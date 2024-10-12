from django.db import models
from django.utils import timezone

class Categoria(models.Model):
    nombre = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.nombre

class Post(models.Model):
    titulo = models.CharField(max_length=200, null=False, blank=False)
    subtitulo = models.CharField(max_length=200, null=False, blank=False)
    fecha_publicacion = models.DateTimeField(default=timezone.now)
    texto = models.TextField(null=False, blank=False)
    activo = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, default='Sin categoria')
    imagen = models.ImageField(upload_to='media', null=False, blank=False, default='static/img/post_default.jpg')
    publicado = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('publicado',)

    def __str__(self):
        return self.titulo
    
    def delete(self, using=None, keep_parents=False):
        self.imagen.delete()
        super().delete()