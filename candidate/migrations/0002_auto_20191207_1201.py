# Generated by Django 2.2.7 on 2019-12-07 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='question1_id',
        ),
        migrations.RemoveField(
            model_name='candidate',
            name='question2_id',
        ),
        migrations.RemoveField(
            model_name='candidate',
            name='question3_id',
        ),
    ]
