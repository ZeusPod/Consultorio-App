# Generated by Django 4.2.7 on 2024-01-05 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('citas', '0002_alter_cita_modification_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cita',
            name='modification_date',
            field=models.DateField(auto_now=True),
        ),
    ]