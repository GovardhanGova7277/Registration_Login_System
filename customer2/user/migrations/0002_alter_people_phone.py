# Generated by Django 5.0.1 on 2024-02-28 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='phone',
            field=models.BigIntegerField(unique=True),
        ),
    ]
