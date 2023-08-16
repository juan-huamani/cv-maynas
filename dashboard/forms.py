from django import forms
from .models import Persons,PersonsDocumentation,WorkExperiences, Companies, Education, Institutions, Languages, Idiomas

class PersonRegistrationForm(forms.ModelForm):

    class Meta:
        model = Persons
        fields = ('first_name', 'last_name', 'address', 'email', 'phone', 'departament_fk', 'province_fk', 'district_fk')
        labels = {
            'first_name': 'Nombres',
            'last_name': 'Apellidos',
            'address': 'Direccion',
            'email': 'Correo',
            'phone': 'Celular',
            'departament_fk': 'Departamento',
            'province_fk': 'Provincia',
            'district_fk': 'Distrito',
        }

class PersonsDocumentationForm(forms.ModelForm):

    class Meta:
        model = PersonsDocumentation
        fields = ('document_fk', 'number')
        labels = {
            'document_fk': 'Tipo de Documento',
            'number': 'N° de Documento',
        }
# Work Experience
class WorkExperienceForm(forms.ModelForm):
    class Meta:
        model = WorkExperiences
        fields = ['company_start_date', 'company_end_date']
        widgets = {
            'company_start_date': forms.DateInput(attrs={'type': 'date'}),
            'company_end_date': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'company_start_date': 'Fecha de Inicio',
            'company_end_date': 'Fecha de Fin',
        }

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Companies
        fields = ['name']
        labels = {
            'name': 'Nombre de la Empresa',
        }
# Education
class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['institution_start_date', 'institution_end_date']
        widgets = {
            'institution_start_date': forms.DateInput(attrs={'type': 'date'}),
            'institution_end_date': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'institution_start_date': 'Fecha de Inicio',
            'institution_end_date': 'Fecha de Fin',
        }

class CapacitationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['hours','institution_start_date', 'institution_end_date']
        widgets = {
            'institution_start_date': forms.DateInput(attrs={'type': 'date'}),
            'institution_end_date': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'hours': 'Horas Lectivas',
            'institution_start_date': 'Fecha de Inicio',
            'institution_end_date': 'Fecha de Fin',
        }
        error_messages = {
            'hours': {
                'required': 'Este campo es obligatorio. Por favor ingresa las horas lectivas.',
            },
        }

class InstitutionForm(forms.ModelForm):
    class Meta:
        model = Institutions
        fields = ['name']
        labels = {
            'name': 'Nombre de la Institucion',
        }
# Languages
class LanguagesForm(forms.ModelForm):
    class Meta:
        model = Languages
        fields = ['name','level_fk']
        labels = {
            'name': 'Idioma',
            'level_fk': 'Nivel',
        }