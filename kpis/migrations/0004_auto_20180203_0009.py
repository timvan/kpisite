# Generated by Django 2.0 on 2018-02-02 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kpis', '0003_auto_20180202_2149'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activity',
            old_name='count',
            new_name='activity_value',
        ),
    ]
