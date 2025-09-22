from django.shortcuts import render, get_object_or_404
from .models import Category, Article

# Create your views here.
def list(request):
    articles = Article.objects.all().order_by('-created_at')
    return render(request, 'articles/list.html', {
        'title': 'Artículos',
        'articles': articles
    })

def category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    # articles = Article.objects.filter(categories=category).order_by('-created_at')
    return render(request, 'categories/category.html', {
        'title': 'Categoría',        
        'category': category,        
    })