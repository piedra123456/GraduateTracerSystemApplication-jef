# Generated by Django 3.2.7 on 2022-01-20 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracer', '0016_workexperiences_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workexperiences',
            name='description',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
