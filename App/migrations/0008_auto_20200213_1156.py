# Generated by Django 2.2 on 2020-02-13 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0007_auto_20200213_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parking',
            name='All_time',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='parking',
            name='P_Money',
            field=models.FloatField(blank=True, max_length=8, null=True),
        ),
    ]
