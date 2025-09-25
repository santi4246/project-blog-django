from django.contrib import admin
from .models import Page


# Configuración extra para modelos
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'visible', 'created_at', 'updated_at')
    search_fields = ('title',)
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('title', 'content')
    list_filter = ('visible',)    

# Configuración del panel de administración
title = "Proyecto con Django"
subtitulo = "Panel de administración"
admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = subtitulo

# Register your models here.
admin.site.register(Page, PageAdmin)