# Generated by Django 3.2.9 on 2021-12-03 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machines',
            name='description',
            field=models.CharField(max_length=200),
        ),
    ]
