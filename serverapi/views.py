from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from Student import models as st
from Books import models as bk
from Borrows import models as bw
from Users import models as ur
import json
import time
from django.views.decorators.csrf import csrf_exempt
from django.middleware.csrf import get_token
from tools import DataLoad
# from serverapi.urls import urlpatterns
# Create your views here.
def test(request):
    return HttpResponse('this is test msg'.encode())

def home(request):
    return HttpResponse('nihao'.encode())
def stringmode(request,data):
    accept=request.META.get("HTTP_ACCEPT")
    print (type(accept),accept)
    print (data)
    if accept=='string/html':
        result=""
        for item in data:
            # print (type(item['pk']))
            result+=item['pk']+" "
            for (k, v) in item['fields'].items():

                result+= str(v)+' '
            result+='$'
        return result
    else:
        return data
def studentall(request):
    itemList = st.StudentInfo.objects.filter()
    json_data=serializers.serialize("json",itemList)
    data=json.loads(json_data)
    result=stringmode(request, data)
    # print(result)
    return HttpResponse(result)
@csrf_exempt
def studentquery(request):
    sid=request.POST.get('sid')
    print('************',sid)
    print('************',request.POST)
    print('************')

    itemList=st.StudentInfo.objects.filter(sid=sid)
    if len(itemList)!=0:
        json_data = serializers.serialize("json", itemList)
        data=json.loads(json_data)
        print("这是studentQuery",data)
        result = stringmode(request, data)
        return HttpResponse(result)
    else:
        return HttpResponse("404".encode())


@csrf_exempt
def studentadd(request):
    if request.method=='GET':
        get_token(request)
        return HttpResponse()
    elif request.method=='POST':
        sid=request.POST.get('sid')
        print("---->",sid)
        sname=request.POST.get('sname')
        smajor=request.POST.get('smajor')
        sclass=request.POST.get('sclass')
        sphone=request.POST.get('sphone')
        obj=st.StudentInfo.objects.filter(sid=sid)
        # return HttpResponse('getit!'.encode())
        msg = {}
        if len(obj)!=0:
            return HttpResponse('已经有这个学生了！'.encode())
        else:
            try:
                st.StudentInfo.objects.create(sid=sid,sname=sname,smajor=smajor,sclass=sclass,sphone=sphone)
            except Exception as e:
                return HttpResponse(e)
            obj=st.StudentInfo.objects.all()
            for item in obj:
                print(item.sid)
            return HttpResponse('添加成功！'.encode())
@csrf_exempt
def studentdel(request):

        sid = request.POST.get('sid')
        obj = st.StudentInfo.objects.filter(sid=sid)
        if len(obj) != 0:
            st.StudentInfo.objects.filter(sid=sid).delete()
        return HttpResponse('删除成功！'.encode())

@csrf_exempt
def studentedit(request):
    sid=request.POST.get('sid')
    print(sid)
    obj = st.StudentInfo.objects.filter(sid=sid)
    msg = ''
    if len(obj) == 0:

        msg= '没有这个学生!'
    else:
        obj=obj[0]
        obj.sname = request.POST.get('sname')
        obj.smajor = request.POST.get('smajor')
        obj.sclass = request.POST.get('sclass')
        obj.sphone = request.POST.get('sphone')
        obj.save()
        msg = """修改成功!"""
    return HttpResponse(msg.encode())
@csrf_exempt
def studentDelAll(request):
    obj = st.StudentInfo.objects.filter()
    if len(obj) != 0:
        st.StudentInfo.objects.filter().delete()
    msg =  '全部删除成功！'
    return HttpResponse(msg.encode())



def bookall(request):
    itemList = bk.BookInfo.objects.filter()
    json_data=serializers.serialize("json",itemList)
    data=json.loads(json_data)
    result=stringmode(request,data)
    if(data==""):
        data="没有图书信息！"
    return HttpResponse(result)
@csrf_exempt
def bookquery(request):
    bid=request.POST.get('bid')
    print('************',bid)
    print('************',request.POST)
    print('************')

    itemList=bk.BookInfo.objects.filter(bid=bid)
    json_data = serializers.serialize("json", itemList)
    data=json.loads(json_data)
    data=stringmode(request,data)
    return HttpResponse(data)


@csrf_exempt
def bookadd(request):

    bid=request.POST.get('bid')
    bname=request.POST.get('bname')
    bauthor=request.POST.get('bauthor')
    bpublisher=request.POST.get('bpublisher')
    bdate=request.POST.get('bdate')
    bstore=request.POST.get('bstore')
    obj=bk.BookInfo.objects.filter(bid=bid)
    msg = {}
    if len(obj)!=0:
        return HttpResponse('已经有这本图书了！'.encode())
    else:
        bk.BookInfo.objects.create(bid=bid,bname=bname,bauthor=bauthor,bpublisher=bpublisher,bdate=bdate,bstore=bstore)
        obj=bk.BookInfo.objects.all()
        for item in obj:
            print(item.bid)
        return HttpResponse('添加成功！'.encode())
@csrf_exempt
def bookdel(request):

        bid = request.POST.get('bid')
        obj = bk.BookInfo.objects.filter(bid=bid)
        if len(obj) != 0:
            bk.BookInfo.objects.filter(bid=bid).delete()
            return HttpResponse('书号：%s 删除成功！'%(bid).encode())
        else:
            return HttpResponse('没有这本书！'.encode())

@csrf_exempt
def bookedit(request):
    bid=request.POST.get('bid')
    obj = bk.BookInfo.objects.filter(bid=bid)
    msg = ''
    if len(obj) == 0:
        msg= '没有这本图书!'
    else:
        obj=obj[0]
        obj.bname = request.POST.get('bname')
        obj.bauthor = request.POST.get('bauthor')
        obj.bpublisher = request.POST.get('bpublisher')
        obj.bdate = request.POST.get('bdate')
        obj.bstore=request.POST.get('bstore')
        obj.save()
        msg = """修改成功!"""
    return HttpResponse(msg.encode())

@csrf_exempt
def bookDelAll(request):
    obj = bk.BookInfo.objects.filter()
    if len(obj) != 0:
        bk.BookInfo.objects.filter().delete()
    msg =  '全部删除成功！'
    return HttpResponse(msg.encode())


@csrf_exempt
def borrowbooks(request):
    bwid = time.time()
    bid = request.POST.get('bid')
    sid = request.POST.get('sid')
    stu = st.StudentInfo.objects.filter(sid=sid)
    book = bk.BookInfo.objects.filter(bid=bid)
    msg = ''
    if len(stu) != 0 and book != len(book) != 0:
        if book[0].bborrow < book[0].bstore:
            bw.BorrowInfo.objects.create(bwid=bwid, sid=stu[0], bid=book[0])
            book[0].bborrow = book[0].bborrow + 1
            book[0].save()
            msg = '借书成功！'

        else:

            msg = '借书失败!图书已经都借出去了！'
    else:
        msg = '借书失败！没有这本书，或者没这个学生！'

    return HttpResponse(msg.encode())


@csrf_exempt
def returnbooks(request):
    msg = {}


    bid = request.POST.get('bid')
    sid = request.POST.get('sid')
    stu = st.StudentInfo.objects.filter(sid=sid)
    book = bk.BookInfo.objects.filter(bid=bid)
    print("sid",sid,"bid",bid)
    if len(stu) != 0 and len(book) != 0:
        obj = bw.BorrowInfo.objects.filter(sid=stu[0], bid=book[0])

        if len(obj) != 0:
            book[0].bborrow = book[0].bborrow - 1 if book[0].bborrow > 0 else 0
            book[0].save()
            bw.BorrowInfo.objects.filter(bwid=obj[0].bwid).delete()
            msg='还书成功！'
        else:
            msg = '还书失败！您没借过这本书！'
    else:
        msg = '还书失败！'
    return HttpResponse(msg.encode())


@csrf_exempt
def allborrows(request):
    objList = bw.BorrowInfo.objects.filter()
    json_data = serializers.serialize("json", objList,use_natural_foreign_keys=True)

    return HttpResponse(json_data)


@csrf_exempt
def queryborrow(request):
    if request.method == 'GET':
        return render(request, 'borrowQuery.html')
    if request.method == 'POST':
        bid = request.POST.get('bid')
        sid = request.POST.get('sid')
        if bid == '' and sid == '':
            objList = bw.BorrowInfo.objects.filter()
        elif bid != '' and sid == '':
            objList = bw.BorrowInfo.objects.filter(bid=bid)
        elif bid == '' and sid != '':
            objList = bw.BorrowInfo.objects.filter(sid=sid)
        else:
            objList = bw.BorrowInfo.objects.filter(bid=bid, sid=sid)
        json_data = serializers.serialize("json", objList,use_natural_foreign_keys=True)
    return HttpResponse(json_data)

#以下部分还未实现
def backupsbook(request):

    return HttpResponse('图书备份成功！'.encode())


def recoverybook(request):
    DataLoad.BookLoad()
    return HttpResponse('图书恢复成功！'.encode())

def recoveryborrow(request):
    return HttpResponse('操作成功！'.encode())
def backupsborrow(request):
    return HttpResponse('操作成功！'.encode())

def recoverystudent(request):
    DataLoad.StudentLoad()
    return HttpResponse('学生恢复成功！'.encode())

def backupsstudent(request):
    return HttpResponse('学生备份成功！'.encode())


def signup(request):
    return HttpResponse('注册成功！'.encode())
def logout(request):
    return HttpResponse('退出成功！'.encode())
#以上部分还未实现
@csrf_exempt
def login(request):
    try:
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        print(user,pwd)

        obj = ur.UserInfo.objects.filter(username=user, password=pwd)
        if len(obj)!=0:
            print('这个用户登录了！', user, pwd)
            request.session['username'] = user
            request.session['is_login'] = True
            request.session.set_expiry(0)
            return HttpResponse('200#登录成功！'.encode())
        else:
            print('有个用户登录失败！',user,pwd)
            return HttpResponse('401#用户名或密码错误！'.encode())
    except Exception as e:
        print (e)
    return HttpResponse("登录失败，未知错误！".encode())



