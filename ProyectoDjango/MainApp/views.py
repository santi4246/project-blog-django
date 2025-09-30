from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm  
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

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
    if request.user.is_authenticated:
        return redirect("inicio")
    else:        
        register_form = RegisterForm()
        if request.method == 'POST':
            register_form = RegisterForm(request.POST)
            if register_form.is_valid():
                register_form.save()
                messages.success(request, 'Te has registrado correctamente')
                return redirect("inicio")
        return render(request, 'Users/register.html', {
        'title': 'Registro',
        'register_form': register_form
        })

def login_page(request):
    if request.user.is_authenticated:
        return redirect("inicio")
    else:        
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('inicio')
            else:
                messages.warning(request, 'Datos ingresados incorrectamente')
                return redirect('login')
        return render(request, 'Users/login.html', {
        'title': 'Iniciar sesión',
        })

def logout_user(request):
    logout(request)
    return redirect('login')