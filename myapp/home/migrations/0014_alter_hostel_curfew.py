# Generated by Django 4.2.7 on 2023-12-04 15:57

from django.db import migrations, models
import home.models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0013_alter_hostel_curfew"),
    ]

    operations = [
        migrations.AlterField(
            model_name="hostel",
            name="curfew",
            field=models.TimeField(default=home.models.get_default_curfew_time),
        ),
    ]