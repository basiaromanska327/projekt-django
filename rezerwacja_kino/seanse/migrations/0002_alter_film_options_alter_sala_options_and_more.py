# Generated by Django 5.1.4 on 2024-12-21 18:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seanse', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='film',
            options={'verbose_name_plural': 'Filmy'},
        ),
        migrations.AlterModelOptions(
            name='sala',
            options={'verbose_name_plural': 'Sale'},
        ),
        migrations.AlterModelOptions(
            name='seans',
            options={'verbose_name_plural': 'Seanse'},
        ),
        migrations.CreateModel(
            name='Rezerwacja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liczba_biletow', models.IntegerField(verbose_name='Liczba biletów')),
                ('seans', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='seanse.seans')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
