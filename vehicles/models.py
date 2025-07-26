from django.db import models
from users.models import User

CATEGORY_CHOICES = [
    (1, 'Intermunicipal'),
    (2, 'Metropolitana'),
    (3, 'Campus interior'),
]

class Vehicle(models.Model):
    driver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='vehicles')
    category = models.IntegerField(choices=CATEGORY_CHOICES)  # Example categories: 1 - intermunicipal, 2 - metropolitan, 3 - Campus interior
    color = models.CharField(max_length=50)
    license_plate = models.CharField(max_length=50, unique=True)
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    soat_due_date = models.DateField()
    technical_mechanical_due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, default=None)

    class Meta:
        db_table = 'vehicles'