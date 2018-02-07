# Generated by Django 2.0 on 2018-02-06 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kpis', '0023_auto_20180206_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kpi',
            name='periodicity',
            field=models.CharField(choices=[('YR', 'Yearly'), ('DY', 'Daily'), ('WK', 'Weekly'), ('MH', 'Monthly')], default='DY', max_length=2),
        ),
    ]