# Generated by Django 2.0 on 2018-02-04 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kpis', '0012_auto_20180204_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kpi',
            name='periodicity',
            field=models.CharField(choices=[('YR', 'Yearly'), ('DY', 'Daily'), ('WK', 'Weekly'), ('MH', 'Monthly')], default='DY', max_length=2),
        ),
    ]
