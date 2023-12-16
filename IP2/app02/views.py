import datetime
import random

from django.shortcuts import render, redirect, HttpResponse
from app01.models import *
# Create your views here.

def recharge(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        numb = request.POST.get('numb')
        if not all([user, numb]):
            return render(request, 'recharge.html', {'msg': '数据有遗落'})
        a = User.objects.filter(username=user)
        if not a:
            return render(request, 'recharge.html', {'msg': '没有该账号'})
        b = CarMy.objects.filter(token=numb)
        if not b:
            return render(request, 'recharge.html', {'msg': '不存在此卡密'})
        e = CarMy.objects.get(token=numb)
        d = User.objects.get(username=user)
        d.quantity = int(d.quantity)+int(e.quota)
        d.save()
        c = CarMy.objects.get(token=numb).delete()
        return render(request, 'recharge.html', {'msg': '充值成功！！！'})
    else:
        return render(request, 'recharge.html')

def login2(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not all([username, password]):
            return render(request, 'login2.html', {'msg': '数据有遗落'})
        a = User.objects.filter(username=username, password=password)
        if not a:
            return render(request, 'login2.html', {'msg': '账号或密码错误'})
        bb = User.objects.get(username=username, password=password)
        b = datetime.datetime.now().strftime('%Y-%m-%d')
        bb.recent_login = b
        bb.save()
        request.session['user']={'user': username, 'password': password}
        return redirect('qingt:information')
    return render(request, 'login2.html')

def information(request):
    a = request.session['user'].get('user')
    print(a)
    ip = User.objects.get(username=a)

    return render(request, 'information.html', {'a': a, 'ip':ip})

def logout(request):
    request.session['user']=None
    return redirect('qingt:login2')

def pwd(request):
    if request.method=='POST':
        a = request.session['user'].get('user')
        b = request.session['user'].get('password')
        aa = User.objects.get(username=a, password=b)
        pwd = request.POST.get('pwd')
        pwd1 = request.POST.get('pwd1')
        security = request.POST.get('security')
        if not int(pwd) == int(pwd1):
            return render(request, 'pwd.html', {'msg': '两次密码输入不一致！'})
        if not aa.security == security:
            return render(request, 'pwd.html', {'msg': '密保错误！'})
        aa.password = pwd
        aa.save()
        request.session['user'] = None
        return render(request, 'pwd.html', {'msg': '修改成功'})
    else:
        return render(request, 'pwd.html')

def ip1(request):
    a = request.session['user'].get('user')
    b = request.session['user'].get('password')
    return render(request, 'apiwz.html', {'api': "您的api:" + "\n" + "http://127.0.0.1:8000/xiao/ip1/?user=" + a + "&pwd=" + b})
