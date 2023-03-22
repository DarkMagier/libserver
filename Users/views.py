from django.shortcuts import render,HttpResponse
from Users import models
# Create your views here.

def login(request):
    if request.method=='GET':
        return render(request,'login.html',{'titile':'登录-图书馆管理系统'})
    elif request.method=='POST':
        user=request.POST.get('user')
        pwd=request.POST.get('pwd')
        # print(user,pwd)
        obj=models.UserInfo.objects.filter(username=user,password=pwd)
        # print(obj)
        msg={}
        if len(obj)!=0:
            request.session['username']=user
            request.session['is_login']=True
            request.session.set_expiry(0)
            msg['title'] = '登录成功！'
            msg['msg'] = '登录成功'
        else:
            msg['title'] = '登录失败！'
            msg['msg'] = '用户名或密码错误 '
        msg['url'] = '/'
        msg['btnm'] = '返回'
        return render(request, 'OpResponse.html', msg)



def signup(request):
    if request.method=='GET':
        return render(request,'signup.html',{'titile':'注册-图书馆管理系统'})
    elif request.method=='POST':
        user=request.POST.get('user')
        pwd=request.POST.get('pwd')
        print(user,pwd)

        obj = models.UserInfo.objects.filter(username=user)
        # print(obj)
        msg = {}
        if len(obj) == 0:
            models.UserInfo.objects.create(username=user, password=pwd)
            msg['title'] = '注册成功！'
            msg['msg'] = '注册成功'
        else:
            msg['title'] = '注册失败！'
            msg['msg'] = '注册失败！该用户已经被注册！ '
        msg['url'] = '/'
        msg['btnm'] = '返回'
        return render(request, 'OpResponse.html', msg)

def logout(request):
    request.session.clear()
    request.session.set_expiry(0.1)
    msg={}
    msg['title'] = '退出成功！'
    msg['msg'] = '退出成功！ '


    msg['url'] = '/'
    msg['btnm'] = '返回'
    return render(request, 'OpResponse.html', msg)


