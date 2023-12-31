from django.shortcuts import render, redirect, get_object_or_404
from .models import Persons, PersonsDocumentation, PersonsType, Documents, WorkExperiences, Education, Idiomas
from .forms import PersonRegistrationForm, PersonsDocumentationForm, WorkExperienceForm, CompanyForm, EducationForm, InstitutionForm, LanguagesForm, CapacitationForm

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from dateutil.relativedelta import relativedelta
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def home_view(request):
    # Asegúrate de que el usuario esté autenticado antes de acceder a la página home
    if request.user.is_authenticated:
        return render(request, 'dashboard/home.html')
    else:
        return redirect('login')  # Redirige al usuario al inicio de sesión si no está autenticado

@login_required
def personal_info_view(request):
    try:
        person = Persons.objects.get(user_fk=request.user.id)
        # person_attributes = vars(person)
        # print(person_attributes)
        documentation = PersonsDocumentation.objects.get(documentation_id=person.documentation_fk_id)

    except (Persons.DoesNotExist, PersonsDocumentation.DoesNotExist):
        person = None
        documentation = None

    if request.method == 'POST':
        person_form = PersonRegistrationForm(request.POST, instance=person)
        documentation_form = PersonsDocumentationForm(request.POST, instance=documentation)

        if person_form.is_valid() and documentation_form.is_valid():
            
            person_type_fk_id=1
            person_type_fk = PersonsType.objects.get(person_type_id=person_type_fk_id)
            # Guardar los datos en la tabla PersonsDocumentation
            documentation = documentation_form.save(commit=False)
            
            # Obtener la instancia de Documents relacionada con PersonsDocumentation
            document_instance = Documents.objects.get(document_id=documentation.document_fk_id)
            documentation.document_fk = document_instance

            documentation.save()

            # Guardar los datos en la tabla Persons
            person = person_form.save(commit=False)
            person.user_fk = request.user
            person.documentation_fk = documentation
            person.person_type_fk=person_type_fk
            person.save()

            # Redirige a una página de éxito o realiza alguna otra acción
            return redirect('personal_info')
    else:
        person_form = PersonRegistrationForm(instance=person)
        documentation_form = PersonsDocumentationForm(instance=documentation)

    return render(request, 'dashboard/personal_info.html', {
        'person_form': person_form,
        'documentation_form': documentation_form,
    })

@login_required
def work_experience_view(request):

    experiencias = WorkExperiences.objects.filter(user_fk=request.user)

    if request.method == 'POST':
        work_experience_form = WorkExperienceForm(request.POST)
        company_form = CompanyForm(request.POST)
        if work_experience_form.is_valid() and company_form.is_valid():
            empresa = company_form.save(commit=False)
            empresa.state_fk_id = 1
            empresa.save()
            experiencia = work_experience_form.save(commit=False)
            experiencia.user_fk = request.user
            experiencia.state_fk_id = 1
            experiencia.company_fk = empresa
            experiencia.save()
            return redirect('work_experience')
    else:
        work_experience_form = WorkExperienceForm()
        company_form = CompanyForm()

    return render(request, 'dashboard/work_experience.html', {
        'work_experience_form': work_experience_form,
        'company_form': company_form,
        'experiencias': experiencias,
    })

@login_required
def eliminar_experiencia(request, experiencia_id):
    experiencia = get_object_or_404(WorkExperiences, pk=experiencia_id)
    experiencia.delete()
    return redirect('work_experience')

@login_required
def capacitation_view(request):
    educaciones = Education.objects.filter(user_fk=request.user).exclude(hours__isnull=True)

    if request.method == 'POST':
        education_form = CapacitationForm(request.POST)
        institution_form = InstitutionForm(request.POST)
        if education_form.is_valid() and institution_form.is_valid():
            institucion = institution_form.save(commit=False)
            institucion.state_fk_id = 1
            institucion.save()
            educacion = education_form.save(commit=False)
            educacion.user_fk = request.user
            educacion.state_fk_id = 1
            educacion.institution_fk = institucion
            educacion.save()
            return redirect('capacitation')
        else:
            try:
                education_form.clean()  # Esto provocará la validación y posiblemente la excepción
            except ValidationError as e:
                error_message = e.messages[0]  # Captura el primer mensaje de error
                return render(request, 'dashboard/capacitation.html', {'education_form': education_form,'institution_form': institution_form,'educaciones': educaciones, 'error_message': error_message})
    else:
        education_form = CapacitationForm()
        institution_form = InstitutionForm()

    return render(request, 'dashboard/capacitation.html', {
        'education_form': education_form,
        'institution_form': institution_form,
        'educaciones': educaciones,
    })

@login_required
def education_view(request):
    educaciones = Education.objects.filter(user_fk=request.user).exclude(hours__isnull=False)

    if request.method == 'POST':
        education_form = EducationForm(request.POST)
        institution_form = InstitutionForm(request.POST)
        if education_form.is_valid() and institution_form.is_valid():
            institucion = institution_form.save(commit=False)
            institucion.state_fk_id = 1
            institucion.save()
            educacion = education_form.save(commit=False)
            educacion.user_fk = request.user
            educacion.state_fk_id = 1
            educacion.institution_fk = institucion
            educacion.save()
            return redirect('education')
    else:
        education_form = EducationForm()
        institution_form = InstitutionForm()

    return render(request, 'dashboard/education.html', {
        'education_form': education_form,
        'institution_form': institution_form,
        'educaciones': educaciones,
    })

@login_required
def eliminar_educacion(request, educacion_id):
    educacion = get_object_or_404(Education, pk=educacion_id)
    educacion.delete()
    return redirect('education')

@login_required
def language_view(request):
    idiomas = Idiomas.objects.filter(user_fk=request.user)
    if request.method == 'POST':
        languages_form = LanguagesForm(request.POST)
        if languages_form.is_valid():
            lenguaje = languages_form.save(commit=False)
            lenguaje.save()
            Idiomas.objects.create(
                user_fk=request.user,
                language_fk=lenguaje,
                state_fk_id=1
            )
            return redirect('language')
    else:
        languages_form = LanguagesForm()

    return render(request, 'dashboard/language.html', {
        'languages_form': languages_form,
        'idiomas': idiomas,
    })

@login_required
def eliminar_language(request, language_id):
    language = get_object_or_404(Idiomas, pk=language_id)
    language.delete()
    return redirect('language')

@login_required
def export_to_pdf(request):
    
    #education = Education.objects.filter(user_fk=request.user)
    educations_without_hours = Education.objects.filter(user_fk=request.user, hours__isnull=True)
    educations_with_hours = Education.objects.filter(user_fk=request.user, hours__isnull=False)

    person = Persons.objects.filter(user_fk=request.user)
    experience = WorkExperiences.objects.filter(user_fk=request.user)
    for ex in experience:
        start_date = ex.company_start_date
        end_date = ex.company_end_date
        time_delta = relativedelta(end_date, start_date)

        ex.time_translated = format_time(time_delta.years, time_delta.months, time_delta.days)
    
    language = Idiomas.objects.filter(user_fk=request.user)
    
    template_path = 'dashboard/cv_template.html'  # Reemplaza 'ruta_de_tu_plantilla.html' con la ruta de tu plantilla HTML
    context = {'person': person, 'education': educations_with_hours,'education_without_hours':educations_without_hours, 'experience' : experience, 'language' : language}  # Aquí puedes pasar los datos que necesites a tu plantilla HTML

    # Carga la plantilla HTML
    template = get_template(template_path)
    html = template.render(context)

    css = '<link rel="stylesheet" href="{}">'.format(
        request.build_absolute_uri('/static/css/template.css')
    )
    img_tag = '<img src="{}" alt="Logo">'.format(
        request.build_absolute_uri('/static/img/logo.png')
    )
    
    # Reemplaza el lugar donde deseas que aparezca la imagen en el HTML generado
    html = html.replace('<!-- INSERT_LOGO_HERE -->', img_tag)
    html = css + html

    # Crea un objeto HttpResponse con tipo MIME para el PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="curriculum_vitae.pdf"'

    # Genera el PDF
    pisa.CreatePDF(html, dest=response)

    return response

def format_time(years, months, days):
    time_parts = []

    if years == 1:
        time_parts.append("1 año")
    elif years > 1:
        time_parts.append(f"{years} años")

    if months == 1:
        time_parts.append("1 mes")
    elif months > 1:
        time_parts.append(f"{months} meses")

    if days == 1:
        time_parts.append("1 día")
    elif days > 1:
        time_parts.append(f"{days} días")

    if len(time_parts) == 1:
        return time_parts[0]
    elif len(time_parts) == 2:
        return f"{time_parts[0]} y {time_parts[1]}"
    else:
        return f"{', '.join(time_parts[:-1])}, y {time_parts[-1]}"