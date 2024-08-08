# Generated by Django 5.1 on 2024-08-08 07:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=255)),
                ('subject_url', models.SlugField(max_length=255, unique=True)),
                ('subject_qrcode', models.ImageField(blank=True, upload_to='Subject QRs')),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.instructor')),
            ],
        ),
    ]
