# Generated by Django 4.0.5 on 2022-11-07 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracer', '0066_advertise_job_sent_list'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advertise',
            name='job_sent_list',
        ),
        migrations.AddField(
            model_name='user',
            name='job_sent_list',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
