# Generated by Django 3.2.6 on 2021-09-25 22:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subscribers',
            options={'verbose_name': 'Suscriptor', 'verbose_name_plural': 'Subscriptores'},
        ),
        migrations.AlterField(
            model_name='subscribers',
            name='email',
            field=models.EmailField(max_length=254, validators=[django.core.validators.EmailValidator]),
        ),
    ]
