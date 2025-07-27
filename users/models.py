from django.db import models
from django.contrib.auth.models import AbstractUser
from universities.models import University
from roles.models import Role


class User(AbstractUser):
    email = models.EmailField(unique=True)
    second_name = models.CharField(max_length=150, blank=True, null=True)
    second_last_name = models.CharField(max_length=150, blank=True, null=True)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    institutional_email = models.EmailField(blank=True, null=True)
    student_code = models.CharField(max_length=20,blank=True, null=True)
    academic_register_photo = models.ImageField(upload_to='academic_register_photos/', blank=True, null=True)
    institutional_id_photo = models.ImageField(upload_to='institutional_carnet_photos/', blank=True, null=True)
    identification_document = models.CharField(max_length=20, unique=True)
    university = models.ForeignKey(University, on_delete=models.SET_NULL, blank=True, null=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']