from django.db import models
from django.core.validators import MinValueValidator
from machine.models import Machine
from material.models import Material
from service.models import Service
from provider.models import Provider


class OccurrenceCategory(models.TextChoices):
    PREVENTIVE_MAINTENANCE = "preventive_maintenance", "Manutenção preventiva"
    CORRECTIVE_MAINTENANCE = "corrective_maintenance", "Manutenção corretiva"
    MANUFACTURE = "manufacture", "Fabricação"
    PERIODIC_ACTIONS = "periodic_actions", "Ações periódicas"


class Occurrence(models.Model):
    description = models.CharField(max_length=500)
    total_cost = models.DecimalField(
        decimal_places=2,
        max_digits=11,
        validators=[MinValueValidator(0)],
    )
    category = models.CharField(choices=OccurrenceCategory.choices, max_length=50)
    machine = models.ForeignKey(Machine, null=True, on_delete=models.SET_NULL)
    downtime = models.IntegerField(validators=[MinValueValidator(0)])
    datetime = models.DateTimeField(auto_now_add=True)

    @property
    def category_label(self):
        return OccurrenceCategory(self.category).label


class OccurrenceService(models.Model):
    occurrence = models.ForeignKey(Occurrence, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, null=True, on_delete=models.SET_NULL)
    provider = models.ForeignKey(Provider, null=True, on_delete=models.SET_NULL)


class OccurrenceMaterial(models.Model):
    occurrence = models.ForeignKey(Occurrence, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, null=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField(validators=[MinValueValidator(0)])
