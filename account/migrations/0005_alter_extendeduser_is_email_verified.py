# Generated by Django 4.1.7 on 2023-04-13 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_remove_extendeduser_account_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extendeduser',
            name='is_email_verified',
            field=models.BooleanField(default=True),
        ),
    ]
