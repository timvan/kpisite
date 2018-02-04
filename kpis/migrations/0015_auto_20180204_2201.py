# Generated by Django 2.0 on 2018-02-04 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kpis', '0014_auto_20180204_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kpi',
            name='periodicity',
            field=models.CharField(choices=[('MH', 'Monthly'), ('YR', 'Yearly'), ('WK', 'Weekly'), ('DY', 'Daily')], default='DY', max_length=2),
        ),
    ]