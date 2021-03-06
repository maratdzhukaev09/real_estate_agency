# Generated by Django 2.2.4 on 2020-07-14 16:54

from django.db import migrations

import phonenumbers

def make_owner_phone_pure(apps, schema_editor):
    Flat = apps.get_model("property", "Flat")
    for flat in Flat.objects.all():
        phonenumber = phonenumbers.parse(flat.owners_phonenumber, 'RU')
        if phonenumbers.is_valid_number(phonenumber):
            phonenumber_format = phonenumbers.PhoneNumberFormat.E164
            flat.owner_phone_pure = phonenumbers.format_number(phonenumber, phonenumber_format)
            flat.save()
        else:
            flat.owner_phone_pure = None
            flat.save()

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_auto_20200714_1945'),
    ]

    operations = [
        migrations.RunPython(make_owner_phone_pure)
    ]
