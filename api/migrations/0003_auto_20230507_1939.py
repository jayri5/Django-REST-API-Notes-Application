# Generated by Django 3.0.2 on 2023-05-07 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_note'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='company',
        ),
        migrations.DeleteModel(
            name='Company',
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]