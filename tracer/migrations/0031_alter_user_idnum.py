# Generated by Django 4.1 on 2022-08-25 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracer', '0030_user_idnum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='IDNum',
            field=models.PositiveIntegerField(blank=True, null=True, unique=True),
        ),
    ]
