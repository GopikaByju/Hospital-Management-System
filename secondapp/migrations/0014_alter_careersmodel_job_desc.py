# Generated by Django 5.1.4 on 2025-01-30 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secondapp', '0013_alter_careersmodel_job_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='careersmodel',
            name='job_desc',
            field=models.TextField(blank=True, null=True),
        ),
    ]
