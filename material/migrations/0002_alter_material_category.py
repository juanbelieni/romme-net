# Generated by Django 3.2.9 on 2021-12-01 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('material', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='category',
            field=models.CharField(choices=[(1, 'eletric'), (2, 'hidraulic'), (3, 'mechanic'), (4, 'eletronic'), (5, 'pneumatic'), (6, 'consumable')], max_length=1),
        ),
    ]
