# Generated by Django 3.2.10 on 2022-01-08 05:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_rename_notes_note'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='note',
            options={'verbose_name': 'notes', 'verbose_name_plural': 'notes'},
        ),
    ]
