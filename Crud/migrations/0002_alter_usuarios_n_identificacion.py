# Generated by Django 3.2 on 2023-01-15 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Crud', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='N_Identificacion',
            field=models.CharField(max_length=13, primary_key=True, serialize=False),
        ),
    ]