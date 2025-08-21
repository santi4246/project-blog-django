from django.db import models

# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    content = models.TextField(verbose_name="Contenido")
    slug = models.CharField(max_length=250, verbose_name="URL amigable")
    public = models.CharField(unique=True, max_length=150, verbose_name="Publicado")
    visible = models.BooleanField(default=True, verbose_name="Visible")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Página"
        verbose_name_plural = "Páginas"
        ordering = ['-created_at']

    def __str__(self):
        return self.title