from django.shortcuts import render, get_object_or_404
from .models import Category, Article
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login/')
def list(request):
    # Sacar artículos
    articles = Article.objects.all().order_by('-created_at')
    # Paginar artículos
    paginator = Paginator(articles, 3)
    # Recoger número de página
    page = request.GET.get('page')
    page_articles = paginator.get_page(page)
    categories = Category.objects.filter(articles__public=True).distinct()
    return render(request, 'articles/list.html', {
        'title': 'Artículos',
        'articles': page_articles,
        'categories': categories,
    })

@login_required(login_url='/login/')
def category(request, category_id):    
    category = get_object_or_404(Category, pk=category_id)
    # articles = Article.objects.filter(categories=category).order_by('-created_at')
    return render(request, 'categories/category.html', {
        'title': 'Categoría',        
        'category': category,
    })

@login_required(login_url='/login/')
def article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'articles/detalle.html', {
        'title': article.title,
        'article': article
    })