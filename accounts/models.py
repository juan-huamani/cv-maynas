from django.contrib.auth.models import AbstractUser
from django.db import models
from settings.models import States, UsersType

# Create your models here.

class Users(AbstractUser):
    email = models.EmailField(max_length=150, unique=True)
    user_type_fk = models.ForeignKey(UsersType, models.DO_NOTHING, db_column='user_type_fk', db_comment='Foreign key referencing the user type in the user types table')
    state_fk = models.ForeignKey(States, models.DO_NOTHING, db_column='state_fk', db_comment='Foreign key referencing the state in the states table')

    # Añadir related_name para evitar conflictos
    groups = models.ManyToManyField('auth.Group', related_name='users_custom')
    user_permissions = models.ManyToManyField('auth.Permission', related_name='users_custom')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','password'] 




