# Generated by Django 4.1 on 2023-08-09 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Behealthy", "0004_alter_user_medical_profile_contactnumber"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user_medical_profile",
            name="contactNumber",
            field=models.CharField(max_length=13),
        ),
    ]
