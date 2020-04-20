import time

from alipay import AliPay
from django.core.checks import messages
from django.forms import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.utils.datetime_safe import datetime

from App.models import Car, Parking, Car_w
from Parking.settings import ALIPAY_APPID, APP_PRIVATE_KEY, ALIPAY_PUBLIC_KEY
from utils.user_utils import my_login


def hello(request):
    return HttpResponse('hello')


def index(request):
    cw=Car_w.objects.filter(Car_w_status=True)
    return render(request, 'index.html',context=locals())


def car_in(request):
    if request.method == 'GET':
        car_ws = Car_w.objects.filter(Car_w_status=True)
        return render(request, 'car_in.html', context=locals())
    elif request.method == 'POST':
        car_no = request.POST.get('car_no')
        car_length = request.POST.get('car_length')
        car_color = request.POST.get('car_color')
        car_type = request.POST.get('car_type')
        car_w_no = request.POST.get('car_w_no')

        car_w_test = Car_w.objects.get(Car_w_no=car_w_no)
        if float(car_length) > car_w_test.Car_w_length:
            info = '车辆长度过长'
            car_ws = Car_w.objects.filter(Car_w_status=True)
            return render(request, 'car_in.html', context=locals())
        else:
            p_cars = Parking.objects.filter(Cat_status=True)
            for p_car in p_cars:
                if car_no == p_car.P_Car_no.Car_no:
                    info = '已有这辆车'
                    car_ws = Car_w.objects.filter(Car_w_status=True)
                    return render(request, 'car_in.html', context=locals())
            else:
                cars = Car.objects.all()
                for car in cars:
                    if (car_no == car.Car_no):
                        car_re = Car.objects.get(Car_no=car_no)
                        car_re.Car_type = car_type
                        car_re.Car_color = car_color
                        car_re.Car_length = car_length
                        car_re.save()
                        break
                else:
                    Car.objects.create(Car_no=car_no, Car_color=car_color, Car_type=car_type, Car_length=car_length)

                car_no = Car.objects.get(Car_no=car_no)
                parking = Parking.objects.create(P_Car_no=car_no, P_Car_w_no=car_w_test)

                car_w_test.Car_w_status = False
                car_w_test.save()
                info = '添加成功'
                car_ws = Car_w.objects.filter(Car_w_status=True)
                return render(request, 'car_in.html', context=locals())


def car_out(request):
    if request.method == 'GET':
        car_nos = Parking.objects.filter(Cat_status=True)
        return render(request, 'car_out.html', context=locals())
    elif request.method == 'POST':
        car_no = request.POST.get('car_no')
        print(car_no)
        # car_rm = Parking.objects.filter(P_Car_no=car_no).first()
        car_rm = Parking.objects.filter(Cat_status=True).get(P_Car_no__Car_no=car_no)
        # print(car_rm)
        car_w = Car_w.objects.get(Car_w_no=car_rm.P_Car_w_no.Car_w_no)
        car_w.Car_w_status = True
        car_w.save()
        intime = car_rm.In_time
        outtime = datetime.now()
        car_rm.Out_time = outtime
        intime_str = intime.strftime("%Y-%m-%d %H:%M:%S")
        outtime_str = outtime.strftime("%Y-%m-%d %H:%M:%S")
        intime_f = intime.timestamp()
        outtime_f = outtime.timestamp()
        alltime = outtime_f - intime_f
        alltime = int(alltime / 60 + 1)
        time_hour = int(alltime / 60)
        time_min = alltime - time_hour * 60
        pri_time = int(alltime / 60 + 1)
        Money = pri_time * car_rm.P_price
        car_rm.P_Money = Money
        car_rm.All_time = alltime
        car_rm.Cat_status = False
        car_rm.save()

        print(intime, outtime)
        print(type(intime))
        hourtime = alltime / 60 + 1
        context = {
            'car_no': car_no,
            'intime': intime,
            'outtime': outtime,
            'alltime': hourtime,
            'money': Money,
        }
        # print(type(car_no), car_no)
        return render(request, 'pay.html', context=locals())


def pay(request):
    money = request.GET.get('money')
    # 构建支付的客户端 AlipayClient
    alipay_client = AliPay(
        appid=ALIPAY_APPID,
        app_notify_url=None,  # 默认回调url
        app_private_key_string=APP_PRIVATE_KEY,
        # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
        alipay_public_key_string=ALIPAY_PUBLIC_KEY,
        sign_type="RSA2",  # RSA 或者 RSA2
        debug=False  # 默认False
    )
    # 使用Alipay进行支付请求的发起
    subject = '停车费13'
    # 客户端操作
    no = str(int(time.time()))
    order_string = alipay_client.api_alipay_trade_page_pay(
        out_trade_no=no,
        total_amount=money,
        subject=subject,
        return_url="http://127.0.0.1:8000/index",
        notify_url=""  # 可选, 不填则使用默认notify url
    )
    return redirect('https://openapi.alipaydev.com/gateway.do?' + order_string)


