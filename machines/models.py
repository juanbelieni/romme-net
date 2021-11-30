from django.db import models

# Model: machine
# Columns: id, name, description
class Machines(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
