# Generated by Django 4.0.6 on 2022-09-08 11:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hospital', '0001_initial'),
        ('doctor', '0006_test_specimen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report_PDF',
            fields=[
                ('report_pdf_id', models.AutoField(primary_key=True, serialize=False)),
                ('specimen_id', models.CharField(blank=True, max_length=200, null=True)),
                ('specimen_type', models.CharField(blank=True, max_length=200, null=True)),
                ('collection_date', models.CharField(blank=True, max_length=200, null=True)),
                ('receiving_date', models.CharField(blank=True, max_length=200, null=True)),
                ('test_name', models.CharField(blank=True, max_length=200, null=True)),
                ('result', models.CharField(blank=True, max_length=200, null=True)),
                ('unit', models.CharField(blank=True, max_length=200, null=True)),
                ('referred_value', models.CharField(blank=True, max_length=200, null=True)),
                ('delivery_date', models.CharField(blank=True, max_length=200, null=True)),
                ('doctor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='doctor.doctor_information')),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hospital.patient')),
            ],
        ),
    ]