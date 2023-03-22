from django.shortcuts import render,HttpResponse,render_to_response
from Borrows import models
from Student import models as st
from Books import models as bk
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
import time
# Create your views here.
def home(request):
    return render(request,'borrowsHome.html',{'titile':'Home-图书借阅'})

def borrow(request):
    if request.method=='GET':
        return render(request, 'borrowbooks.html', {'titile': '借书-图书管理系统'})
    elif request.method=='POST':
        bwid=time.time()
        bid=request.POST.get('bid')
        sid=request.POST.get('sid')
        stu= st.StudentInfo.objects.filter(sid=sid)
        book=bk.BookInfo.objects.filter(bid=bid)
        msg={}
        if len(stu)!=0 and book !=len(book)!=0:
            if book[0].bborrow < book[0].bstore:
                models.BorrowInfo.objects.create(bwid=bwid,sid=stu[0],bid=book[0])
                book[0].bborrow=book[0].bborrow+1
                book[0].save()
                msg['title'] = '借书成功！'
                msg['msg'] ='借书成功！'
            else:
                msg['title'] = '借书成功！'
                msg['msg'] = '借书失败!图书已经都借出去了！'
        else:
            msg['title'] = '借书成功！'
            msg['msg'] = '借书失败！'
        msg['url'] = '/borrows/borrows'
        msg['btnm'] = '返回'
        return render(request, 'OpResponse.html', msg)


def returnbooks(request):
    if request.method=='GET':
        return render(request, 'borrowReturn.html', {'titile': '还书-图书管理系统'})
    elif request.method=='POST':
        msg={}
        bid=request.POST.get('bid')
        sid=request.POST.get('sid')
        stu= st.StudentInfo.objects.filter(sid=sid)
        book=bk.BookInfo.objects.filter(bid=bid)
        if len(stu)!=0 and len(book)!=0:
            obj=models.BorrowInfo.objects.filter(sid=stu[0],bid=book[0])
            book[0].bborrow=book[0].bborrow-1 if book[0].bborrow>0 else 0
            book[0].save()
            if len(obj)!=0:
                models.BorrowInfo.objects.filter(bwid=obj[0].bwid).delete()
                msg['title'] = '还书成功！'
                msg['msg'] = '还书成功！'
            else:
                msg['title'] = '还书失败！'
                msg['msg'] = '您没借过这本书！'
        else:
            msg['title'] = '还书失败！'
            msg['msg'] = '还书失败！'
        msg['url'] = '/borrows/'
        msg['btnm'] = '返回'
        return render(request, 'OpResponse.html', msg)


def allborrows(request):

    objList=models.BorrowInfo.objects.filter()
    paginator = Paginator(objList, 15)
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

    return render_to_response('borrowsall.html', {'contacts': contacts, 'page_range': page_range, 'page_sum': page_sum})

    # return render(request,'borrowsall.html',{'itemList':objList})

def queryborrow(request):
    if request.method=='GET':
        return render(request,'borrowQuery.html')
    if request.method=='POST':
        bid=request.POST.get('bid')
        sid=request.POST.get('sid')
        print("-->borrow query ",bid,sid)
        if bid==''and sid=='':
            print("-->run borrow query 1")
            objList = models.BorrowInfo.objects.filter()
        elif bid!=''and sid=='':
            print("-->run borrow query 2")
            objList = models.BorrowInfo.objects.filter(bid=bid)
        elif bid==''and sid!='':
            print("-->run borrow query 3")
            objList = models.BorrowInfo.objects.filter(sid=sid)
        else:
            print("-->run borrow query 4")
            objList = models.BorrowInfo.objects.filter(bid=bid, sid=sid)
        print("-->result borrow query ",len(objList))
        paginator = Paginator(objList, 15)
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

        return render_to_response('borrowsall.html',
                                  {'contacts': contacts, 'page_range': page_range, 'page_sum': page_sum})

def recoveryborrow(request):
    return HttpResponse('操作成功！'.encode())
def backupsborrow(request):
    return HttpResponse('操作成功！'.encode())