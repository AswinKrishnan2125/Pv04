# Generated by Django 4.2.7 on 2023-12-04 15:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0012_alter_hostel_curfew"),
    ]

    operations = [
        migrations.AlterField(
            model_name="hostel",
            name="curfew",
            field=models.TimeField(default=datetime.time(15, 56, 55, 700815)),
        ),
    ]