# Generated by Django 2.0 on 2018-02-04 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kpis', '0011_auto_20180204_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kpi',
            name='periodicity',
            field=models.CharField(choices=[('WK', 'Weekly'), ('YR', 'Yearly'), ('MH', 'Monthly'), ('DY', 'Daily')], default='DY', max_length=2),
        ),
    ]