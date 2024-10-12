from django.contrib import admin

# Register your models here.
from .models import Categoria, Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id','titulo', 'subtitulo', 'activo', 'categoria','fecha_publicacion','publicado','imagen','texto')
    search_fields = ('titulo', 'subtitulo', 'categoria')
    list_filter = ('categoria', 'fecha_publicacion')

admin.site.register(Categoria)