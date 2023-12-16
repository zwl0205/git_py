from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect
import re


class M2(MiddlewareMixin):
    def process_request(self, request):
        a = re.match('/xiao/', request.path)
        if a:
            print(a)
        else:
            if request.path == '/qingt/login2/':
                print('登陆界面')
            else:
                try:
                    a = request.session['user']
                    print(a)
                except:
                    return redirect('qingt:login2')
                a = request.session['user']
                if a:
                    print(11111111111111111111111111)
                else:
                    return redirect('qingt:login2')


