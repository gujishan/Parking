# Generated by Django 2.2 on 2020-02-13 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0008_auto_20200213_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parking',
            name='All_time',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
    ]
