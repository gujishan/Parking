# Generated by Django 2.2 on 2020-02-13 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0006_auto_20200213_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parking',
            name='P_Money',
            field=models.FloatField(blank=True, max_length=16, null=True),
        ),
    ]
