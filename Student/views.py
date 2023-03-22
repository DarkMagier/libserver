from django.shortcuts import render,HttpResponse,redirect,render_to_response
from django.utils.safestring import mark_safe
# Create your views here.
from Student import models
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from tools import DataLoad
def student(request):
    print('-->student!')
    # return HttpResponse('OK')
    return render(request,'studentHome.html')

def addastudent(request):
    if request.method=='GET':
        # msg = {}
        # msg['title'] = '添加成功！'
        # msg['msg'] = '添加成功'
        # msg['url'] = request.get_full_path()
        # return render(request, 'OpResponse.html', msg)
        return render(request,'studentadd.html')
    elif request.method=='POST':
        sid=request.POST.get('sid')
        sname=request.POST.get('sname')
        smajor=request.POST.get('smajor')
        sclass=request.POST.get('sclass')
        sphone=request.POST.get('sphone')
        obj=models.StudentInfo.objects.filter(sid=sid)
        msg = {}
        if len(obj)!=0:
            msg['title'] = '添加失败！'
            msg['msg'] = '添加失败，已经有这学生的信息了！'
        else:
            models.StudentInfo.objects.create(sid=sid,sname=sname,smajor=smajor,sclass=sclass,sphone=sphone)
            obj=models.StudentInfo.objects.all()
            for item in obj:
                print(item.sid)

            msg['title']='添加成功！'
            msg['msg']='添加成功'
        msg['url']=request.get_full_path()
        msg['btnm']='返回'
        return render(request, 'OpResponse.html', msg)

def delastudent(request):
    if request.method=='GET':
        return render(request, 'studentdel.html')
    elif request.method=='POST':
        sid=request.POST.get('sid')
        obj = models.StudentInfo.objects.filter(sid=sid)
        if len(obj) != 0:
            models.StudentInfo.objects.filter(sid=sid).delete()
        msg = {}
        msg['title']='删除成功！'
        msg['msg']='删除成功'
        msg['url']=request.get_full_path()
        msg['btnm']='返回'
        return render(request, 'OpResponse.html', msg)

def studentall(request):
    itemList = models.StudentInfo.objects.filter()
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


    return render_to_response('studentall.html', {'contacts': contacts, 'page_range':page_range,'page_sum': page_sum})
def delallstudent(request):

    if request.method=='GET':
        return render(request, 'studentpredellall.html')
    elif request.method=='POST':

        sid=request.POST.get('sid')
        obj = models.StudentInfo.objects.filter()
        if len(obj) != 0:
            models.StudentInfo.objects.filter().delete()
        msg = {}
        msg['title']='全部删除成功！'
        msg['msg']='全部删除成功'
        msg['url']='/student/'
        msg['btnm']='返回'
        return render(request, 'OpResponse.html', msg)

def queryastudent(request):
    if request.method=='GET':
        return render(request,'studentQuery.html')
    elif request.method=='POST':
        sid=request.POST.get('sid')
        obj = models.StudentInfo.objects.filter(sid=sid)
        if len(obj)==0:
            msg = {}
            msg['title'] = '没有这个学生！'
            msg['msg'] = '没有这个学生!'
            msg['url'] = '/student/queryastudent'
            msg['btnm'] = '返回'
            return render(request, 'OpResponse.html', msg)
        else:
            return  render(request, 'studentQueryResult.html', {'item':obj[0]})

def editastudent(request):
    if request.method=='GET':
        return render(request,'studenteditQuery.html')
    elif request.method=='POST':
        sid=request.POST.get('sid')
        obj = models.StudentInfo.objects.filter(sid=sid)
        if len(obj) == 0:
            msg = {}
            msg['title'] = '没有这个学生！'
            msg['msg'] = '没有这个学生!'
            msg['url'] = '/student/editastudent'
            msg['btnm'] = '返回'
            return render(request, 'OpResponse.html', msg)
        isedit=request.POST.get('isedit')
        msg=""
        if isedit=="N":
            msg="""修改学生信息"""
            return render(request,'studentEditPage.html',{'item':obj[0],'msg':msg})
        elif isedit=='Y':
            sid = request.POST.get('sid')
            obj = models.StudentInfo.objects.filter(sid=sid)
            if len(obj) == 0:
                msg = {}
                msg['title'] = '没有这个学生！'
                msg['msg'] = '没有这个学生!'
                msg['url'] = '/student/editastudent'
                msg['btnm'] = '返回'
                return render(request, 'OpResponse.html', msg)
            obj=obj[0]
            obj.sname = request.POST.get('sname')
            obj.smajor = request.POST.get('smajor')
            obj.sclass = request.POST.get('sclass')
            obj.sphone = request.POST.get('sphone')
            obj.save()
            msg = """修改成功!"""
            return render(request, 'studentEditPage.html', {'item': obj, 'msg': msg})

def recoverystudent(request):
    DataLoad.StudentLoad()
    return HttpResponse('操作成功！'.encode())

def backupsstudent(request):
    return HttpResponse('操作成功！'.encode())



