# Generated by Django 2.1.3 on 2019-03-17 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_mentor',
            new_name='is_mod',
        ),
    ]
