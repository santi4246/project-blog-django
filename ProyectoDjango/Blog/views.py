from django.shortcuts import render
from .models import Category, Article

# Create your views here.
def list(request):
    articles = Article.objects.all().order_by('-created_at')
    return render(request, 'articles/list.html', {
        'title': 'Artículos',
        'articles': articles
    })