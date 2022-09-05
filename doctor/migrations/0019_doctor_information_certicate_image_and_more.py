# Generated by Django 4.0.6 on 2022-09-05 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0018_experience_education'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor_information',
            name='certicate_image',
            field=models.ImageField(blank=True, default='doctors_certificate/default.png', null=True, upload_to='doctors_certificate/'),
        ),
        migrations.AddField(
            model_name='doctor_information',
            name='register_status',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]