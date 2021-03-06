from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from App.models import Login
from utils.user_utils import my_login


def login(request):
    if request.method == 'POST':
        username = request.POST.get('user_name', None)
        password = request.POST.get('pass_word', None)
        if username and password:
            username = username.strip()
            try:
                user = Login.objects.get(name=username)
            except:
                info = "请输入正确的用户名"
                return render(request, 'login.html', context=locals())
            if user.password == password:
                request.session['login_user_name']=username
                request.session.set_expiry(0)
                return render(request,'root.html')
            else:
                info = '请输入正确的密码'
                return render(request, 'login.html', context=locals())
    return render(request, 'login.html')

@my_login
def register(request):
    if request.method == 'POST':
        username = request.POST.get('user_name', None)
        password = request.POST.get('pass_word', None)
        if len(username) > 16 or len(password) > 16:
            info = "账号和密码要小于16位的英文或数字"
            return render(request, "register.html", context=locals())
        else:
            login = Login()
            login.name = username
            login.password = password
            login.save()
            success = "添加成功"
            return render(request, 'register.html', context=locals())
    return render(request, 'register.html')

@my_login
def root(request):
    return render(request, 'root.html')

@my_login
def ul(request):
    root=request.session.get("login_user_name")
    if root=='root':
        info='root'
        return render(request,'ul.html',context=locals())
    else:
        return render(request,'ul.html')

@my_login
def welcome(request):
    username=request.session.get("login_user_name")
    return render(request,'welcome.html',context=locals())


def get_all(request):
    login=Login.objects.all()
    return render(request,'all_login.html',context=locals())