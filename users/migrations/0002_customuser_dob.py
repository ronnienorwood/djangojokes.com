# Generated by Django 4.2 on 2023-04-24 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='dob',
            field=models.DateField(blank=True, null=True, verbose_name='Date of Birth'),
        ),
    ]