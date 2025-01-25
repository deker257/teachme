from django.db import models
from django.contrib.auth.models import AbstractUser

# TEACHER MODEL.
class Users(AbstractUser):
    # CHAMPS DE LA TABLE TEACHERS
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    username = models.CharField(max_length=150, unique=True, blank=True)
    email = models.CharField(max_length=150, unique=True, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    sex = models.CharField(max_length=30, choices=[('Homme', 'Homme'), ('Femme', 'Femme')])
    profil = models.ImageField(upload_to='profiles/', blank=True)
    origins = models.CharField(max_length=100)
    sector = models.CharField(max_length=100) 
    biography = models.TextField(max_length=500)
    password = models.CharField(max_length=128)
    students = models.PositiveIntegerField(default=0)
    teachers = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = 'users' # Spécifie le nom de la table

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


