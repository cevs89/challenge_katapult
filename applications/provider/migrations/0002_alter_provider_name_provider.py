# Generated by Django 4.1.7 on 2023-02-28 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("applications_provider", "0001_init_provider"),
    ]

    operations = [
        migrations.AlterField(
            model_name="provider",
            name="name_provider",
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
