from django.db import models
from django import forms

# Model: material
# Columns: id, name, category
class Material(models.Model):
    class MaterialCategory(models.TextChoices):
        ELECTRIC = "electric", "Elétrico"
        HIDRAULIC = "hidraulic", "Hidráulico"
        MECHANIC = "mechanic", "Mecânico"
        ELETRONIC = "eletronic", "Eletrônico"
        PNEUMATIC = "pneumatic", "Pneumático"
        CONSUMABLE = "consumable", "Consumível"

    name = models.CharField(max_length=200)
    category = models.CharField(
        max_length=200,
        choices=MaterialCategory.choices,
    )
