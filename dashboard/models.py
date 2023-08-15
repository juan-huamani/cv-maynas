from django.db import models
from settings.models import States
from accounts.models import Users

# Create your models here.

class Departments(models.Model):
    departament_id = models.AutoField(primary_key=True, db_comment='The unique identifier for the department')
    name = models.CharField(max_length=50, db_comment='The name of the department')
    state_fk = models.ForeignKey(States, models.DO_NOTHING, db_column='state_fk', db_comment='Foreign key referencing the state of the district in the states table')

    class Meta:
        db_table = 'departments'
    
    def __str__(self):
        return self.name

class Provinces(models.Model):
    province_id = models.AutoField(primary_key=True, db_comment='he unique identifier for the province.')
    name = models.CharField(max_length=50, db_comment='The name of the province')
    departament_fk = models.ForeignKey(Departments, models.DO_NOTHING, db_column='departament_fk')
    state_fk = models.ForeignKey(States, models.DO_NOTHING, db_column='state_fk', db_comment='Foreign key referencing the state of the district in the states table')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'provinces'

class Districts(models.Model):
    district_id = models.AutoField(primary_key=True, db_comment='The unique identifier for the district')
    name = models.CharField(max_length=50, db_comment='The name of the district')
    province_fk = models.ForeignKey(Provinces, models.DO_NOTHING, db_column='province_fk', db_comment='Foreign key referencing the province of the department in the provinces table')
    state_fk = models.ForeignKey(States, models.DO_NOTHING, db_column='state_fk', db_comment='Foreign key referencing the state of the district in the states table')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'districts'


class Documents(models.Model):
    document_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    state_fk = models.ForeignKey(States, models.DO_NOTHING, db_column='state_fk')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'documents'

class PersonsType(models.Model):
    person_type_id = models.AutoField(primary_key=True, db_comment='The unique identifier for the person type.')
    name = models.CharField(max_length=50, db_comment='The name of the person type.')
    state_fk = models.ForeignKey(States, models.DO_NOTHING, db_column='state_fk', db_comment='Foreign key referencing the state in the states table.')

    class Meta:
        db_table = 'persons_type'


class PersonsDocumentation(models.Model):
    documentation_id = models.AutoField(primary_key=True)
    document_fk = models.ForeignKey(Documents, models.DO_NOTHING, db_column='document_fk')
    number = models.CharField(max_length=30)

    def __str__(self):
        return self.document_fk.name

    class Meta:
        db_table = 'persons_documentation'

class Persons(models.Model):
    person_id = models.AutoField(primary_key=True, db_comment='The unique identifier for the person')
    first_name = models.CharField(max_length=50, db_comment='The first name of the person')
    last_name = models.CharField(max_length=50, db_comment='The last name of the person')
    address = models.CharField(max_length=100, db_comment='The address of the person')
    user_fk = models.ForeignKey(Users, models.DO_NOTHING, db_column='user_fk', db_comment='Foreign key referencing the user associated with this person')
    documentation_fk = models.ForeignKey(PersonsDocumentation, models.DO_NOTHING, db_column='documentation_fk', db_comment='Foreign key referencing the documentation details of the person')
    email = models.CharField(max_length=50, db_comment='The email address of the person')
    phone = models.IntegerField(db_comment='The phone number of the person')
    person_type_fk = models.ForeignKey(PersonsType, models.DO_NOTHING, db_column='person_type_fk', db_comment='Foreign key referencing the type of person in the person types table')
    departament_fk = models.ForeignKey(Departments, models.DO_NOTHING, db_column='departament_fk')
    province_fk = models.ForeignKey(Provinces, models.DO_NOTHING, db_column='province_fk')
    district_fk = models.ForeignKey(Districts, models.DO_NOTHING, db_column='district_fk')

    class Meta:
        db_table = 'persons'


#Work_experience, Education and Languages

class Companies(models.Model):
    company_id = models.AutoField(primary_key=True, db_comment='The unique identifier for the company')
    name = models.CharField(max_length=100, db_comment='The name of the company')
    state_fk = models.ForeignKey(States, models.DO_NOTHING, db_column='state_fk', db_comment='"Foreign key referencing the state of the company in the states table.')

    class Meta:
        db_table = 'companies'

class WorkExperiences(models.Model):
    work_experience_id = models.AutoField(primary_key=True, db_comment='The unique identifier for the company')
    user_fk = models.ForeignKey(Users, models.DO_NOTHING, db_column='user_fk', db_comment='Foreign key referencing the user associated with this person')
    company_fk = models.ForeignKey(Companies, models.DO_NOTHING, db_column='company_fk')
    company_start_date = models.DateField(db_comment='The start date at the company for this CV record')
    company_end_date = models.DateField(db_comment='The end date at the company for this CV record')
    state_fk = models.ForeignKey(States, models.DO_NOTHING, db_column='state_fk', db_comment='"Foreign key referencing the state of the company in the states table.')

    class Meta:
        db_table = 'work_experiences'
        
class Institutions(models.Model):
    institution_id = models.AutoField(primary_key=True, db_comment='The unique identifier for the institution')
    name = models.CharField(max_length=100, db_comment='The name of the institution')
    state_fk = models.ForeignKey(States, models.DO_NOTHING, db_column='state_fk', db_comment='Foreign key referencing the state of the institution in the states table')

    class Meta:
        db_table = 'institutions'

class Education(models.Model):
    education_id = models.AutoField(primary_key=True, db_comment='The unique identifier for the education')
    user_fk = models.ForeignKey(Users, models.DO_NOTHING, db_column='user_fk', db_comment='Foreign key referencing the user associated with this person')
    institution_fk = models.ForeignKey(Institutions, models.DO_NOTHING, db_column='institution_fk')
    institution_start_date = models.DateField(db_comment='The start date at the institution for this CV record')
    institution_end_date = models.DateField(db_comment='The end date at the institution for this CV record')
    hours = models.CharField(max_length=3,blank=True, null=True, db_comment='The duration of education in hours')
    state_fk = models.ForeignKey(States, models.DO_NOTHING, db_column='state_fk', db_comment='"Foreign key referencing the state of the company in the states table.')
    
    class Meta:
        db_table = 'education'

class Levels(models.Model):
    level_id = models.AutoField(primary_key=True, db_comment='The unique identifier for the level')
    name = models.CharField(max_length=50, db_comment='The name of the level')

    class Meta:
        db_table = 'levels'
    def __str__(self):
        return self.name

class Languages(models.Model):
    language_id = models.AutoField(primary_key=True, db_comment='The unique identifier for the language')
    name = models.CharField(max_length=50, db_comment='The name of the language')
    level_fk = models.ForeignKey(Levels, models.DO_NOTHING, db_column='level_fk', db_comment='Foreign key referencing the language level in the levels table')

    class Meta:
        db_table = 'languages'

class Idiomas(models.Model):
    idioma_id = models.AutoField(primary_key=True, db_comment='The unique identifier for the idioma')
    user_fk = models.ForeignKey(Users, models.DO_NOTHING, db_column='user_fk', db_comment='Foreign key referencing the user associated with this person')
    language_fk = models.ForeignKey(Languages, models.DO_NOTHING, db_column='language_fk')
    state_fk = models.ForeignKey(States, models.DO_NOTHING, db_column='state_fk', db_comment='"Foreign key referencing the state of the company in the states table.')

    class Meta:
        db_table = 'languages_user'

