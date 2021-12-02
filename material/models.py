from django.db import models
from django import forms

# Model: material
# Columns: id, name, category
class Material(models.Model):

    STATUS = (
        ("eletric", "Elétrico"),
        ("hidraulic", "Hidráulico"),
        ("mechanic", "Mecânico"),
        ("eletronic", "Eletrônico"),
        ("pneumatic", "Pneumático"),
        ("consumable", "Consumível"),
    )

    name = models.CharField(max_length=200)
    category = models.CharField(
        max_length=200,
        choices=STATUS,
    )
