# Generated by Django 4.2.7 on 2023-12-02 20:26

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0003_remove_grievance_description_remove_grievance_email_and_more"),
    ]

    operations = [
        migrations.DeleteModel(
            name="grievance",
        ),
    ]
