# Generated by Django 3.2.9 on 2021-11-27 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provider',
            name='phone',
            field=models.CharField(max_length=15),
        ),
    ]