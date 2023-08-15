from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from settings.models import UsersType, States
from django.contrib import messages

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        
        if form.is_valid():
            user_type_default = 1  # Reemplaza con el ID del tipo de usuario que deseas asignar por defecto
            user_type_instance = UsersType.objects.get(pk=user_type_default)
            form.instance.user_type_fk = user_type_instance

            state_default = 1  # Reemplaza con el ID del estado que deseas asignar por defecto
            state_instance = States.objects.get(pk=state_default)
            form.instance.state_fk = state_instance
            form.save()
            return redirect('login')  # Redirige al usuario a la página de inicio de sesión después del registro exitoso
    else:
        form = CustomUserCreationForm()
    return render(request, 'register/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('home')  #Redirige al usuario a la página de inicio después del inicio de sesión exitoso
        else:
            # Si el formulario no es válido, los errores se mostrarán en el template automáticamente
            # porque estamos usando el formulario en el contexto de renderización
            #print(form.errors)
            messages.error(request, 'Por favor ingresa un correo y contraseña correctos!')
            pass
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')
 