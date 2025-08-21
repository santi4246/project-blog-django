from django.contrib import admin
from .models import Page

# Register your models here.
admin.site.register(Page)

# Configuración del panel de administración
title = "Proyecto con Django"
subtitulo = "Panel de administración"
admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = subtitulo