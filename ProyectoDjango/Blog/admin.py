from django.contrib import admin
from .models import Category, Article

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name', 'description')

class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('user', 'created_at', 'updated_at')
    search_fields = ('title', 'content', 'user__username', 'categories__name')
    list_display = ('title', 'user', 'created_at', 'public')
    list_filter = ('public', 'categories__name', 'user__username')

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.user = request.user
        super().save_model(request, obj, form, change)

# Configuración extra para modelos
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'visible', 'created_at', 'updated_at')
    search_fields = ('title',)
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('title', 'content')
    list_filter = ('visible',)  

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)