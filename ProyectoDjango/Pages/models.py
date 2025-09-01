from django.db import models
from ckeditor.fields import RichTextField # type: ignore

# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    content = RichTextField(verbose_name="Contenido")
    slug = models.CharField(unique=True, max_length=250, verbose_name="URL amigable")    
    order = models.IntegerField(default=0, verbose_name="Orden")
    visible = models.BooleanField(default=True, verbose_name="Publicado")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Página"
        verbose_name_plural = "Páginas"
        ordering = ['-created_at']

    def __str__(self):
        return self.title