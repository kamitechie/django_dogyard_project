from django.db import models
import base64


class Dog(models.Model):
    dog_id = models.AutoField(primary_key=True)
    photo = models.BinaryField(blank=True, null=True, editable=True)
    dogs_name = models.CharField(max_length=255, blank=True, null=True)
    birth_date = models.DateField()
    gender = models.CharField(max_length=10, blank=True, null=True)
    pool = models.CharField(max_length=10, blank=True, null=True)
    mother = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, related_name='dogs_mother')
    father = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, related_name='dogs_father')

    def __str__(self):
        return self.dogs_name if self.dogs_name else str(self.dog_id)

    def get_photo_base64(self):
        if self.photo:
            return base64.b64encode(self.photo).decode('utf-8')
        else:
            return ''

    class Meta:
        managed = False
        db_table = 'dogs_data'


class Position(models.Model):
    position = models.CharField(unique=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'positions'


class DogPosition(models.Model):
    dog_id = models.ForeignKey('Dog', models.DO_NOTHING, blank=True, null=True)
    position = models.ForeignKey('Position', on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dogs_position'


class MedicalRecord(models.Model):
    id = models.OneToOneField('Dog', on_delete=models.CASCADE, db_column='id', primary_key=True, related_name='medical_record')
    is_neutered = models.BooleanField(blank=True, null=True)
    is_in_rut = models.BooleanField(blank=True, null=True)
    date_of_death = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'basic_hospital_data'


class InjuryType(models.Model):
    type = models.CharField(unique=True, max_length=255)

    def __str__(self):
        return self.type

    class Meta:
        managed = False
        db_table = 'injury'


class InjuryMedicalRecord(models.Model):
    dog = models.ForeignKey('Dog', on_delete=models.CASCADE)
    injury_date = models.DateField()
    vet_checkup_needed = models.BooleanField(blank=True, null=True)
    injury_type = models.ForeignKey('InjuryType', models.DO_NOTHING)
    injury_place = models.CharField(max_length=255, blank=True, null=True)
    drugs_name = models.CharField(max_length=255, blank=True, null=True)
    drugs_time_in_days = models.IntegerField(blank=True, null=True)
    stays_in = models.BooleanField(blank=True, null=True)
    is_case_closed = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'injury_hospital_data'


class AdoptionOwner(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    relocation_place = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'adoption_owners_data'


class AdoptionDog(models.Model):
    dog = models.ForeignKey('Dog', models.DO_NOTHING)
    adoption_date = models.DateField(blank=True, null=True)
    owners = models.ForeignKey('AdoptionOwner', models.DO_NOTHING, blank=True, null=True)
    reason = models.CharField(max_length=255, blank=True, null=True)
    is_adopted = models.BooleanField(blank=True, null=True)
    is_ready_for_adoption = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'adoption_data'


class BorrowPerson(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'borrow_person_data'


class BorrowDog(models.Model):
    dog = models.ForeignKey('Dog', models.DO_NOTHING)
    borrowers = models.ForeignKey('BorrowPerson', models.DO_NOTHING)
    date_of_taking = models.DateField(blank=True, null=True)
    date_of_giving_back = models.DateField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'borrow_data'


class Sibling(models.Model):
    dog_id = models.ForeignKey('Dog', models.DO_NOTHING)
    sibling_id = models.ForeignKey('Dog', models.DO_NOTHING, related_name='other_siblings', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'family_siblings'