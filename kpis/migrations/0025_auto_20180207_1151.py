# Generated by Django 2.0 on 2018-02-07 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kpis', '0024_auto_20180207_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kpi',
            name='periodicity',
            field=models.CharField(choices=[('YR', 'Yearly'), ('WK', 'Weekly'), ('DY', 'Daily'), ('MH', 'Monthly')], default='DY', max_length=2),
        ),
    ]
