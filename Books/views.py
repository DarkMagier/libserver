from django.shortcuts import render,HttpResponse,render_to_response
from Books import models
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from tools import DataLoad
# Create your views here.
def home(request):
    return render(request,'bookHome.html')
def addabook(request):
    if request.method=='GET':
        return render(request, 'bookadd.html', {'titile': '增加图书-图书馆管理系统'})
    elif request.method=='POST':

        bid=request.POST.get('bid')
        obj = models.BookInfo.objects.filter(bid=bid)
        msg = {}
        if len(obj) != 0:
            msg['title'] = '添加失败！'
            msg['msg'] = '添加失败，已经有本图书的信息了！'
        else:
            bname=request.POST.get('bname')
            bauth=request.POST.get('bauth')
            bpub=request.POST.get('bpub')
            bdate=request.POST.get('bdate')
            bstore=request.POST.get('bstore')
            models.BookInfo.objects.create(bid=bid,bname=bname,bauthor=bauth,bpublisher=bpub,bdate=bdate,bstore=bstore)
            msg['title'] = '添加成功！'
            msg['msg'] = '添加成功'
        msg['url'] = request.get_full_path()
        msg['btnm'] = '返回'
        return render(request, 'OpResponse.html', msg)

def delabook(request):
    if request.method == 'GET':
        return render(request, 'bookdel.html')
    elif request.method == 'POST':
        bid = request.POST.get('bid')
        obj = models.BookInfo.objects.filter(bid=bid)
        if len(obj) != 0:
            models.BookInfo.objects.filter(bid=bid).delete()
        msg = {}
        msg['title'] = '删除成功！'
        msg['msg'] = '删除成功'
        msg['url'] = request.get_full_path()
        msg['btnm'] = '返回'
        return render(request, 'OpResponse.html', msg)
def editabook(request):
    if request.method=='GET':
        return render(request,'bookeditQuery.html')
    elif request.method=='POST':
        bid=request.POST.get('bid')
        obj = models.BookInfo.objects.filter(bid=bid)
        if len(obj) == 0:
            msg = {}
            msg['title'] = '没有这本图书！'
            msg['msg'] = '没有这本图书!'
            msg['url'] = '/books/editabook'
            msg['btnm'] = '返回'
            return render(request, 'OpResponse.html', msg)
        isedit=request.POST.get('isedit')
        msg=""
        if isedit=="N":
            msg="""修改图书信息"""
            print(obj[0].bdate)
            return render(request,'bookEditPage.html',{'item':obj[0],'msg':msg})
        elif isedit=='Y':
            bid = request.POST.get('bid')
            obj=obj[0]
            obj.bname    = request.POST.get('bname')
            obj.bauthor = request.POST.get('bauth')
            obj.bpublisher     = request.POST.get('bpub')
            obj.bdate    = request.POST.get('bdate')
            obj.bstore   = request.POST.get('bstore')
            print(request.POST.get('bname'),request.POST.get('bauth'),request.POST.get('bpub'),request.POST.get('bdate'),request.POST.get('bstore'))
            # print(obj[0].bname, obj[0].bauthor, obj[0].bpublisher)
            obj.save()
            # print(obj[0].bname,obj[0].bauthor ,obj[0].bpublisher)
            msg = """修改成功!"""
            obj=models.BookInfo.objects.filter(bid=bid)
            return render(request, 'bookEditPage.html', {'item': obj[0], 'msg': msg})

def queryabook(request):
    if request.method=='GET':
        return render(request,'bookQuery.html')
    elif request.method=='POST':
        bid = request.POST.get('bid')
        obj = models.BookInfo.objects.filter(bid=bid)
        if len(obj) == 0:
            msg = {}
            msg['title'] = '没有这本图书！'
            msg['msg'] = '没有这本图书!'
            msg['url'] = '/books/queryabook'
            msg['btnm'] = '返回'
            return render(request, 'OpResponse.html', msg)
        else:
            return render(request, 'bookQueryResult.html', {'item': obj[0]})


def allbook(request):
    itemList = models.BookInfo.objects.filter()
    paginator = Paginator(itemList, 15)
    # return render(request,'studentall.html',{'itemList':itemList})
    page_sum = paginator.num_pages
    after_range_num = 5
    before_range_num = 5
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        # 建立一个触点，包含sql_result的结果，传入html，使用for语句遍历出最终结果（contacts.object_list 代替原始的sql_result）
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
        # 页面显示数据
    if page >= after_range_num:
        page_range = paginator.page_range[page - after_range_num:page + before_range_num]
    else:
        page_range = paginator.page_range[0:int(page) + before_range_num]

    return render_to_response('bookall.html', {'contacts': contacts, 'page_range': page_range, 'page_sum': page_sum})
    # return render(request, 'bookall.html', {'itemList': itemList})

def delallbook(request):
    if request.method == 'GET':
        return render(request, 'bookpredellall.html')
    elif request.method == 'POST':

        # bid = request.POST.get('bid')
        obj = models.BookInfo.objects.filter()
        if len(obj) != 0:
            models.BookInfo.objects.filter().delete()
        msg = {}
        msg['title'] = '全部删除成功！'
        msg['msg'] = '全部删除成功'
        msg['url'] = '/books/'
        msg['btnm'] = '返回'
        return render(request, 'OpResponse.html', msg)

def backupsbook(request):

    return HttpResponse('操作成功！'.encode())


def recoverybook(request):
    DataLoad.BookLoad()
    return HttpResponse('操作成功！'.encode())

