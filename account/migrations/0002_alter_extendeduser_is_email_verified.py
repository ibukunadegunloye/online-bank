# Generated by Django 4.1.7 on 2023-03-30 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extendeduser',
            name='is_email_verified',
            field=models.BooleanField(default=True),
        ),
    ]
