# Generated by Django 4.0.1 on 2022-02-11 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reminders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reminder',
            name='end_time',
            field=models.TimeField(null=True),
        ),
    ]