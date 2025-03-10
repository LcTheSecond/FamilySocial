# Generated by Django 5.0.7 on 2024-08-04 20:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('date_of_death', models.DateField(null=True)),
                ('phone_number', models.CharField(max_length=20, null=True)),
                ('mobile_number', models.CharField(max_length=20, null=True)),
                ('father', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='father_children', to='profiles.profile')),
                ('mother', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='mother_children', to='profiles.profile')),
                ('spouse', models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to='profiles.profile')),
            ],
            options={
                'verbose_name': 'perfil',
                'verbose_name_plural': 'perfils',
            },
        ),
    ]
