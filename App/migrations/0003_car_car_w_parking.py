# Generated by Django 2.2 on 2020-02-13 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('App', '0002_auto_20200213_1053'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('Car_no', models.CharField(max_length=32, primary_key=True, serialize=False, unique=True)),
                ('Car_length', models.CharField(max_length=32)),
                ('Car_color', models.CharField(max_length=16)),
                ('Car_type', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Car_w',
            fields=[
                ('Car_w_no', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('Car_w_wz', models.CharField(max_length=32)),
                ('Car_w_length', models.CharField(max_length=16)),
                ('Car_w_status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Parking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('In_time', models.DateTimeField()),
                ('Out_time', models.DateTimeField()),
                ('All_time', models.DateTimeField()),
                ('Cat_status', models.BooleanField(default=True)),
                ('P_Money', models.FloatField(max_length=8)),
                ('P_price', models.FloatField(max_length=8)),
                ('P_Car_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.Car')),
                ('P_Car_w_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.Car_w')),
            ],
        ),
    ]
