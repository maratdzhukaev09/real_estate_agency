# Generated by Django 2.2.4 on 2020-07-14 16:32

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('property', '0006_auto_20200714_1919'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='liked_by',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Кто лайкнул'),
        ),
    ]
