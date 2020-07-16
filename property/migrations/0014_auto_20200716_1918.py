# Generated by Django 2.2.4 on 2020-07-16 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0013_auto_20200715_1941'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flat',
            name='owner_name',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owner_phone_pure',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owners_phonenumber',
        ),
        migrations.AlterField(
            model_name='owner',
            name='flats',
            field=models.ManyToManyField(blank=True, db_index=True, related_name='owners', to='property.Flat', verbose_name='Квартиры в собственности'),
        ),
    ]
