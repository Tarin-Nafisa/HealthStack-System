# Generated by Django 4.0.6 on 2022-08-10 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor_information',
            name='degree',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='doctor_information',
            name='visiting_hour',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]