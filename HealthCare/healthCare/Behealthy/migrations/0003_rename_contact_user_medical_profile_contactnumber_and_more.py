# Generated by Django 4.1 on 2023-08-09 02:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Behealthy", "0002_alter_user_medical_profile_table"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user_medical_profile",
            old_name="contact",
            new_name="contactNumber",
        ),
        migrations.RenameField(
            model_name="user_medical_profile",
            old_name="street",
            new_name="streetAddress",
        ),
    ]