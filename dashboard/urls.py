# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home_view, name='home'),
    # Personal Info
    path('personal_info/', views.personal_info_view, name='personal_info'),
    # Work Experience
    path('work_experience/', views.work_experience_view, name='work_experience'),
    path('eliminar_experiencia/<int:experiencia_id>/', views.eliminar_experiencia, name='eliminar_experiencia'),
    # Education
    path('education/', views.education_view, name='education'),
    path('eliminar_educacion/<int:educacion_id>/', views.eliminar_educacion, name='eliminar_educacion'),
    # Language
    path('language/', views.language_view, name='language'),
    path('eliminar_language/<int:language_id>/', views.eliminar_language, name='eliminar_language'),
    path('export-pdf/', views.export_to_pdf, name='export_pdf'),
]
