# Generated by Django 2.2.7 on 2019-12-01 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rsvp',
            name='reg_no',
            field=models.CharField(default='17BCE0267', max_length=9, unique=True),
            preserve_default=False,
        ),
    ]