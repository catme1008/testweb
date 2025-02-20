import re

from django.shortcuts import render, HttpResponse, redirect
from app01.models import *


# Create your views here.
def index(request):
    return HttpResponse("Welcome")


def user_list(request):
    # 去app目录下寻找templates，"user_list.html"
    # 有多个app，根据app的注册顺序挨个寻找
    return render(request, "user_list.html")


def user_add(request):
    return render(request, "user_add.html")


def tpl(request):
    name = "Robot1"
    status = ["Working", "Moving", "Normal"]
    user_info = {"name": "User1", "right": "admin"}
    date_list = [
        {"name": "User1", "right": "admin"},
        {"name": "User2", "right": "root"},
        {"name": "User3", "right": "user"}
    ]
    return render(request, "tpl.html",
                  {"n1": name, "status": status, "n3": user_info, "n4": date_list})


def news(request):
    # 1. 定义一些新闻
    # 2. 可以数据库去取
    # 3. 去爬取新闻，向地址发送请求。
    # requests 模块
    import requests

    res = requests.get(
        "https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=10026765609672&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1")
    data_list = res.content.decode('utf-8')
    data_list = re.sub("fetchJSON_comment98\(", '', data_list)
    data_list = re.sub("\);", '', data_list)
    data_list = data_list.replace('null', 'None')
    data_list = data_list.replace('false', 'False')
    data_dict = eval(data_list)
    return render(request, 'news.html', {"data_dict": data_dict})


def login(request):
    # return render(request, "login.html")
    if request.method == "GET":
        return render(request, "login.html", )
    else:
        # 如果是POST请求
        user_name = request.POST.get("user")
        passwd = request.POST.get("password")
        # 如果
        if user_name == "root" and passwd == "123":
            return HttpResponse("Login Success")
        else:
            # return HttpResponse("Login Fail")
            return render(request, "login.html", {"error_msg": "Invalid!"})


def orm(request):
    # 1.增
    UserInfo.objects.create(name='A', password='123123', age='34')
    UserInfo.objects.create(name='B', password='234cde', age='24')
    UserInfo.objects.create(name='C', password='345fdh', age='21')
    Robots.objects.create(type='Cleaner')
    # 2.删
    Robots.objects.filter(id='2').delete()
    # 3. 查
    # data_list = 【对象，对象，对象】Queryset 类型 all获取所有数据 first
    data_list = Robots.objects.all()
    for obj in data_list:
        print(obj.name, obj.type, obj.reg_time)
    data = Robots.objects.filter(id='1').first()
    print(data.name, data.type, data.reg_time)
    # 4.改
    Robots.objects.all().update(type='Cleaner')
    return HttpResponse("Success!")


def info_list(request):
    # 获取所有用户对象
    data_list = UserInfo.objects.all()
    if request.method == "GET":
        if request.GET.get('uid'):
            uid = request.GET.get('uid')
            UserInfo.objects.filter(id=uid).delete()
            return render(request, "info_list.html", {"data_list": data_list})
        else:
            return render(request, "info_list.html", {"data_list": data_list})
    else:
        user_name = request.POST.get("user")
        passwd = request.POST.get("password")
        age = request.POST.get("age")
        UserInfo.objects.create(name=user_name, password=passwd, age=age)
        data_list = UserInfo.objects.all()
        return render(request, "info_list.html", {"data_list": data_list})
