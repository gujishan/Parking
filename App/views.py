import base64
import datetime
import io
import random
from io import BytesIO
import numpy as np

from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
import matplotlib.pyplot as plt

# Create your views here.
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.dates import DateFormatter
from matplotlib.figure import Figure

from App.models import Car_w, Parking
from utils.user_utils import my_login


def hello(request):
    return HttpResponse('hello')

# 统计数组信息
def all_list(arr):
    result = {}
    for i in set(arr):
        result[i] = arr.count(i)
    return result

# 删除数组中相同的元素
def zl_data(arr):
    zl=[]
    for i in arr:
        if i not in zl:
            zl.append(i)
    return zl
# 分解年月日
def get_year(arr):
    year=arr.split('-',3)[0]
    return year

def get_month(arr):
    month=arr.split('-',3)[1]
    return month

def get_day(arr):
    day=arr.split('-',3)[2]
    return day

# 添加车位
@my_login
def add_parking(request):
    if request.method == 'GET':
        return render(request, 'add_parking.html')
    elif request.method == 'POST':
        # 接受数据
        car_w_no = request.POST.get('car_w_no')
        car_w_length = request.POST.get('car_w_length')
        car_w_wz = request.POST.get('car_w_wz')
        # print(car_w_wz, car_w_length, car_w_no)
        car_ws = Car_w.objects.all()
        for car_w in car_ws:
            if int(car_w_no) == car_w.Car_w_no:
                info = '已经有这个车位'
                return render(request, 'add_parking.html', context=locals())
        else:
            Car_w.objects.create(Car_w_no=car_w_no, Car_w_length=car_w_length, Car_w_wz=car_w_wz)
            info = '添加成功'
        return render(request, 'add_parking.html', context=locals())


# 查看停车位
@my_login
def get_parking(request):
    car_ws = Car_w.objects.all()
    return render(request, 'get_parking.html', context=locals())


# 删除车位
@my_login
def re_parking(request, no):
    car_w = Car_w.objects.get(Car_w_no=no)
    car_w.delete()
    info = "第" + no + "号车位删除成功"
    car_ws = Car_w.objects.all()
    return render(request, 'get_parking.html', context=locals())


# 更改车位信息
@my_login
def update_parking(request, no):
    if request.method == 'POST':
        car_w_length = request.POST.get('car_w_length')
        car_w_wz = request.POST.get('car_w_wz')

        car_w_re = Car_w.objects.get(Car_w_no=no)
        car_w_re.Car_w_length = car_w_length
        car_w_re.Car_w_wz = car_w_wz
        car_w_re.save()
        info = '第' + no + '车位修改成功'
    return render(request, 'update_pa.html', context=locals())


# 显示在停车场的车辆
@my_login
def show_incar(request):
    cars = Parking.objects.filter(Cat_status=True)
    if not cars:
        info = "停车场里没有车"
        return render(request, 'root.html', context=locals())
    else:
        return render(request, 'show_incar.html', context=locals())


# 显示所有车辆
@my_login
def show_allcar(request):
    cars = Parking.objects.all()
    return render(request, 'show_allcar.html', context=locals())


# 显示收入
@my_login
def money(request):
    all_money = 0
    parkings = Parking.objects.filter(Cat_status=False)
    for parking in parkings:
        all_money = all_money + float(parking.P_Money)
    return render(request, 'show_money.html', context=locals())

def tu(request):
    dates=[]
    x_data=[]
    y_data=[]
    parkings=Parking.objects.all()
    for parking in parkings:
        date=parking.In_time
        date=str(date).split(" ",1)[0]
        dates.append(date)
    all=all_list(dates)
    for i in sorted(all.keys()):
        x_data.append(i)
        y_data.append(all[i])
    print(all)
    print(x_data,y_data)
    plt.title('car_num')
    plt.xlabel('date')
    plt.ylabel('num')
    plt.plot(x_data, y_data, color='red', linewidth=2.0, linestyle='--')

    sio = BytesIO()
    plt.savefig(sio, format='png')
    data = base64.encodebytes(sio.getvalue()).decode()
    plt.close()

    return render(request,'tu.html',context=locals())

def tu_find(request):
    datas=[]
    moneyss=[]
    parks=Parking.objects.all()
    for park in parks:
        data=park.Out_time
        data=str(data).split(" ",1)[0]
        datas.append(data)
    zl=zl_data(datas)
    zl.sort()
    for i in zl:
        mons = 0
        print(get_year(i),get_month(i),get_day(i))
        moneys=parks.filter(Out_time__year=get_year(i),Out_time__month=get_month(i),Out_time__day=get_day(i))
        for money in moneys:
            mon=money.P_Money
            mons=mons+mon
        print(mons)
        moneyss.append(mons)
    print(zl)
    print(moneyss)

    x_data=zl
    y_data=moneyss
    plt.title('shouru')
    plt.xlabel('date')
    plt.ylabel('money')
    plt.plot(x_data, y_data, label='shouru',color='red', linewidth=2.0, linestyle='--')

    for a,b in zip(x_data,y_data):
        plt.text(a,b,b,ha='center',va='bottom',fontsize=15)

    sio = BytesIO()
    plt.savefig(sio, format='png')
    data = base64.encodebytes(sio.getvalue()).decode()
    plt.close()

    return render(request,'tu_money.html',context=locals())



def find(request):
    if request.method=="GET":
        return render(request,'find.html')
    else:
        c_no = request.POST.get('car_no')

        cws=Parking.objects.get(Cat_status=True,P_Car_no=c_no)

        return render(request, 'find.html', context=locals())


def find_all(request):
    if request.method=="GET":
        return render(request,'find_all.html')
    elif request.method=="POST":
        c_no = request.POST.get('car_no')
        cws=Parking.objects.filter(P_Car_no=c_no)
        return render(request,'find_all.html',context=locals())


