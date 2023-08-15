from django.urls import path
from . import views
from django.shortcuts import redirect

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('', lambda request: redirect('login/', permanent=False)),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    # Otras URL de tu aplicación
]