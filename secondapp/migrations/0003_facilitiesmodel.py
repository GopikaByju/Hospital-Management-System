# Generated by Django 5.1.4 on 2025-01-12 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secondapp', '0002_gallerymodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacilitiesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
    ]
