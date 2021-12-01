from django.db import models
from django.core.validators import MinValueValidator
from machines.models import Machines
from service.models import Service
from provider.models import Provider


class Occurrence(models.Model):
    """
    Occurrence model

    Fields
    ------
    - description: string, max length of 500
    - down_time: integer, in minutes, min value of 0
    - category: enum(example1, example2, example3)
    - machine: reference to Machine model, nullable, null on delete
    - services: reference to `OccurrenceService` model, one to many
    - created_at: datetime
    """

    class OccurrenceCategory(models.TextChoices):
        """
        Occurrence categories

        Values
        ------
        - example1
        - example2
        - example3
        """

        example1 = "example1"
        example2 = "example2"
        example3 = "example3"

    class OccurrenceService(models.Model):
        """
        Occurrence service model

        Fields
        ------
        - service: reference to Service model, nullable, null on delete
        - provider: reference to Provider model, nullable, null on delete
        - cost: float, min_value=0
        """

        service = models.ForeignKey(Service, null=True, on_delete=models.SET_NULL)
        provider = models.ForeignKey(Provider, null=True, on_delete=models.SET_NULL)
        cost = models.FloatField(validators=[MinValueValidator(0)])

    description = models.CharField(max_length=500)
    down_time = models.IntegerField(validators=[MinValueValidator(0)])
    category = models.CharField(max_length=50)
    machine = models.ForeignKey(Machines, null=True, on_delete=models.SET_NULL)
    services = models.ManyToManyField(OccurrenceService)
    created_at = models.DateTimeField(auto_now_add=True)
