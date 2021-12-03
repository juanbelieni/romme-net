from django.db import models


class MaterialCategory(models.TextChoices):
    ELECTRIC = "electric", "Elétrico"
    HYDRAULIC = "hydraulic", "Hidráulico"
    MECHANIC = "mechanic", "Mecânico"
    ELECTRONIC = "electronic", "Eletrônico"
    PNEUMATIC = "pneumatic", "Pneumático"
    CONSUMABLE = "consumable", "Consumível"


# Model: material
# Columns: id, name, category
class Material(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(choices=MaterialCategory.choices, max_length=50)

    @property
    def category_label(self):
        return MaterialCategory(self.category).label
