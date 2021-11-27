from django.db import models

# Model: provider
# Columns: id, name, phone, address
class Provider(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=200)
