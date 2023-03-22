# coding: utf-8
from libserver.settings import EXCLUDE_URL
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponseRedirect,render
import re
exclued_path = [re.compile(item) for item in EXCLUDE_URL]

class auth(MiddlewareMixin):
    def process_request(self,request):
        print('----->',request.path)
        msg = {}
        for item in exclued_path:
            url=re.search(item,request.path)
            print(item,url)
            if url is not None:
                return

        if request.session.get('is_login',None):
            return
        else:

            msg['title'] = '请登陆后再执行操作！'
            msg['msg'] = '请登陆后再执行操作！ '
            msg['url'] = '/'
            msg['btnm'] = '确定'
            return render(request, 'OpResponse.html', msg)
            # return render(request,'OpResponse.html')