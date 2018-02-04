# Generated by Django 2.0 on 2018-02-04 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kpis', '0013_auto_20180204_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kpi',
            name='periodicity',
            field=models.CharField(choices=[('DY', 'Daily'), ('MH', 'Monthly'), ('WK', 'Weekly'), ('YR', 'Yearly')], default='DY', max_length=2),
        ),
    ]
