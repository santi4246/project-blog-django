from Blog.models import Category, Article

def getCategories(request):
    categories_in_use = Article.objects.filter(public = True).values_list('categories', flat=True)
    categories = Category.objects.filter(articles__public=True, id__in = categories_in_use).distinct()
    return { 'categories': categories, 'ids': categories_in_use }