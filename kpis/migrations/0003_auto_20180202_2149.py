# Generated by Django 2.0 on 2018-02-02 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kpis', '0002_remove_kpi_entry_author'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='KPI_entry',
            new_name='activity',
        ),
    ]
