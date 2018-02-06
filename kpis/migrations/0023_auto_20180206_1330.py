# Generated by Django 2.0 on 2018-02-06 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kpis', '0022_auto_20180206_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kpi',
            name='periodicity',
            field=models.CharField(choices=[('DY', 'Daily'), ('WK', 'Weekly'), ('YR', 'Yearly'), ('MH', 'Monthly')], default='DY', max_length=2),
        ),
    ]