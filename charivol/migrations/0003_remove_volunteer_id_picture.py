# Generated by Django 5.2.1 on 2025-05-22 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('charivol', '0002_alter_volunteer_id_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='volunteer',
            name='id_picture',
        ),
    ]
