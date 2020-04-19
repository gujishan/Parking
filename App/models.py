from django.db import models

# Create your models here.
from django.utils import timezone


# 车位信息表
class Car_w(models.Model):
    Car_w_no = models.IntegerField(primary_key=True, unique=True, null=False, blank=False)
    Car_w_wz = models.CharField(max_length=32)
    Car_w_length = models.FloatField(max_length=16)
    Car_w_status = models.BooleanField(default=True)


# 车辆信息表
class Car(models.Model):
    Car_no = models.CharField(primary_key=True, max_length=32, unique=True)
    Car_length = models.FloatField(max_length=32)
    Car_color = models.CharField(max_length=16)
    Car_type = models.CharField(max_length=32)


# 停车信息表
class Parking(models.Model):
    P_Car_w_no = models.ForeignKey(Car_w, on_delete=models.CASCADE)
    P_Car_no = models.ForeignKey(Car, on_delete=models.CASCADE)
    In_time = models.DateTimeField(auto_now_add=True)
    Out_time = models.DateTimeField(null=True, blank=True)
    All_time = models.CharField(max_length=16, null=True, blank=True)
    Cat_status = models.BooleanField(default=True)
    P_Money = models.FloatField(max_length=8, null=True, blank=True)
    P_price = models.FloatField(max_length=8, null=True, blank=True, default=1.5)


# 管理员账号密码表
class Login(models.Model):
    name = models.CharField(max_length=16)
    password = models.CharField(max_length=16)