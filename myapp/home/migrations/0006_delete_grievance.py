# Generated by Django 4.2.7 on 2023-12-04 10:34

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0005_grievance"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Grievance",
        ),
    ]