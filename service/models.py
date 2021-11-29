from django.db import models

# Model: service
# Columns: id, name
class Service(models.Model):
    name = models.CharField(max_length=200)
