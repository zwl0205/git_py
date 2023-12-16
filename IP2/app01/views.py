from django.contrib import auth
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, HttpResponse
import datetime
# Create your views here.
from app01.models import *
import requests
from lxml import etree
import random
import hashlib
import time

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not all([username, password]):
            context = {'msg': '账号或者密码不能为空'}
            return render(request, 'login.html', context)
        # a = User.objects.filter(username=username, password=password)
        b = auth.authenticate(username=username, password=password)
        # if a:
        #     return redirect('zhian:index')
        if b:
            return redirect('zhian:index')
        context = {'msg': '账号或者密码错误'}
        return render(request, 'login.html', context)

    return render(request, 'login.html')

def index(request):
    user_id = request.GET.get('user_id')
    ip = User.objects.all()
    if user_id:
        ip = User.objects.filter(username=user_id)
    paginator = Paginator(ip, 10)
    page = request.GET.get('page')
    try:
        ip = paginator.page(page)
    except:
        ip = paginator.page(1)

    return render(request, 'index.html',{'ip': ip, 'paginator': paginator})

def add(request):
    if request.method =='POST':
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        qq = request.POST.get('qq')
        security = request.POST.get('security')
        if not all([user, pwd, qq, security]):
            return render(request, 'add.html', {'msg': '有参数有遗落'})
        a = User.objects.filter(username=user)
        if a:
            return render(request, 'add.html', {'msg': '该账号已被注册'})
        ip = User()
        ip.username = user
        ip.password = pwd
        ip.qq = qq
        ip.security = security
        b = datetime.datetime.now().strftime('%Y-%m-%d')
        ip.creation_date = b
        ip.recent_login = b
        ip.quantity = 0
        ip.save()
        return render(request, 'add.html', {'msg': '注册成功'})

    else:
        return render(request, 'add.html')


def update(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        qq = request.POST.get('qq')
        security = request.POST.get('security')
        if not all([user, pwd, qq, security]):
            return render(request, 'add.html', {'msg': '有参数有遗落'})

        ip = User.objects.get(username=user)
        ip.username = user
        ip.password = pwd
        ip.qq = qq
        ip.security = security
        b = datetime.datetime.now().strftime('%Y-%m-%d')
        ip.creation_date = b
        ip.recent_login = b
        ip.quantity = 0
        ip.save()
        return render(request, 'update.html', {'msg': '修改成功'})
    else:
        user = request.GET.get('user')
        ip = User.objects.get(username=user)
        return render(request, 'update.html', {'ip': ip})


def delete(request):
    user = request.GET.get('user')
    a = User.objects.filter(username=user).delete()
    return redirect('xiao:index')

def create(request):
    #代理池
    url = 'https://www.89ip.cn/'
    xieyito = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'
    }
    # 相当于返回值 返回出来的值
    response = requests.get(url=url, headers=xieyito).text

    tree = etree.HTML(response)
    li_list = tree.xpath("//div[3]/div[1]/div/div[1]/table/tbody/tr")
    print(li_list)
    for i in li_list:
        ho = i.xpath('./td[1]/text()')[0]
        ho2 = i.xpath('./td[2]/text()')[0]
        print(ho.strip(), ho2.strip())
        ht = "http://" + ho.strip() + ":" + ho2.strip()
        print(ht)
        try:
            cs = response = requests.get(url='https://www.baidu.com', proxies={"http": ht})
            print(cs)
            ip = IP1()
            ip.ip = ho.strip()
            ip.post = ho2.strip()
            ip.save()
        except:
            print(111111111111111)


def ip1(request):
    #ip
    user = request.GET.get('user')
    pwd = request.GET.get('pwd')
    b = User.objects.filter(username=user, password=pwd)
    if not b:
        return HttpResponse('请输入正确的账号和密码！！！')
    c = User.objects.get(username=user, password=pwd)
    c.quantity = int(c.quantity) - 1
    if int(c.quantity) <= 0:
        return HttpResponse('余额不足，请充值！！！')
    c.save()

    a = random.randint(1, 20)
    ip1 = IP1.objects.get(id=a)
    return HttpResponse(ip1.ip+":"+ip1.post)


def carmy(request):
    #卡密
    if request.method == 'POST':
        user = request.POST.get('user')
        numb = request.POST.get('numb')
        if not all([user, numb]):
            return render(request, 'carmy.html', {'msg': '数据有遗落'})
        for i in range(int(numb)):
            t = int(time.time())
            aa = user +str(t)+str(i)
            m2 = hashlib.md5()
            m2.update(aa.encode('utf-8'))
            aaa = m2.hexdigest()
            b = CarMy()
            b.quota = user
            b.token = aaa
            b.save()

        return render(request, 'carmy.html', {'msg': '添加成功'})
    else:
        return render(request, 'carmy.html')

