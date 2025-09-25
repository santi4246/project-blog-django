from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm  
from .forms import RegisterForm

# Create your views here.
def index(request):
    return render(request, 'MainApp/index.html', {
    'title': 'Inicio',
    })

def about(request):
    return render(request, 'MainApp/about.html', {
    'title': 'Acerca de nosotros',
    })

def register_page(request):
    register_form = RegisterForm()
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            return redirect("inicio")
    return render(request, 'Users/register.html', {
    'title': 'Registro',
    'register_form': register_form
    })