# Generated by Django 4.1.7 on 2023-04-13 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_remove_extendeduser_marital_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='extendeduser',
            old_name='nationality',
            new_name='country',
        ),
    ]
