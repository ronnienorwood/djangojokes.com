# Generated by Django 4.2 on 2023-04-20 20:47

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import jobs.models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='applicant',
            options={},
        ),
        migrations.RemoveField(
            model_name='applicant',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='job',
            name='slug',
        ),
        migrations.AlterField(
            model_name='applicant',
            name='email',
            field=models.EmailField(help_text='A valid email address.', max_length=254),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.job'),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='last_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='start_date',
            field=models.DateField(help_text='The earliest date you can start working.', validators=[jobs.models.validate_future_date]),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='website',
            field=models.URLField(blank=True, validators=[django.core.validators.URLValidator(schemes=['http', 'https'])]),
        ),
    ]
