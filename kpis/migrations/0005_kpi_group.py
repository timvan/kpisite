# Generated by Django 2.0 on 2018-02-03 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kpis', '0004_auto_20180203_0009'),
    ]

    operations = [
        migrations.AddField(
            model_name='kpi',
            name='group',
            field=models.CharField(choices=[('BL', 'blue'), ('RD', 'red'), ('GR', 'green')], default='BL', max_length=2),
        ),
    ]
