# Generated by Django 5.0.1 on 2024-01-30 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='sold',
            field=models.BooleanField(default=False),
        ),
    ]
