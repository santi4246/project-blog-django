from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'MainApp/index.html', {
    'title': 'Inicio',
    })

def about(request):
    return render(request, 'MainApp/about.html', {
    'title': 'Acerca de nosotros',
    })