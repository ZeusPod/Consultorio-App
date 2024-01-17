# Generated by Django 4.2.7 on 2024-01-05 00:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pacientes', '0002_paciente_email_paciente_emergency_contact_and_more'),
        ('roles', '0004_rename_roles_rolesusuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Historia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('register_date', models.DateField(auto_now_add=True)),
                ('anamnesis', models.TextField()),
                ('diagnostic', models.TextField()),
                ('treatment', models.TextField()),
                ('modification_date', models.DateField(auto_now=True)),
                ('medic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='roles.user')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pacientes.paciente')),
            ],
        ),
    ]