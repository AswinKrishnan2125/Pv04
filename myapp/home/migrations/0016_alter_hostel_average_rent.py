# Generated by Django 4.2.7 on 2023-12-04 19:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0015_alter_hostel_curfew"),
    ]

    operations = [
        migrations.AlterField(
            model_name="hostel",
            name="average_rent",
            field=models.PositiveIntegerField(),
        ),
    ]
