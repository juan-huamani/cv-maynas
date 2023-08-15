# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class States(models.Model):
    state_id = models.AutoField(primary_key=True, db_comment='The unique identifier for the state')
    name = models.CharField(max_length=50, db_comment='The name of the state')

    class Meta:
        db_table = 'states'


class UsersType(models.Model):
    user_type_id = models.AutoField(primary_key=True, db_comment='The unique identifier for the user type')
    name = models.CharField(max_length=100, db_comment='The name of the user type.')
    state_fk = models.ForeignKey(States, models.DO_NOTHING, db_column='state_fk', db_comment='Foreign key referencing the state in the states table')

    class Meta:
        db_table = 'users_type'
