from tools import httptest
from Student import models as sm
from Books import models as bkm
def StudentLoad():
    f=open('student.txt','r',encoding='gbk')
    stuList=[]
    for line in f.readlines():
        stu=line.strip().split(' ')
        stuList.append(stu)
    f.close()
    for item in stuList:
        tmp=sm.StudentInfo.objects.filter(sid=item[0])
        # print("student id",item[0],"query len:",len(tmp))
        if len(tmp)==0:
            sm.StudentInfo.objects.create(sid=item[0], sname=item[1], smajor=item[2], sclass=item[3], sphone=item[4])

def BookLoad():
    f = open('book.txt', 'r', encoding='gbk')
    bkList=[]
    for line in f.readlines():
        bk=line.strip().split(' ')
        bkList.append(bk)
    f.close()
    for item in bkList:
        tmp=bkm.BookInfo.objects.filter(bid=item[0])
        if len(tmp)==0:
            date=item[-3]+'-'+item[-2]+'-'+item[-1]
            bkm.BookInfo.objects.create(bid=item[0], bname=item[1], bauthor=item[2], bpublisher=item[3],
                                  bdate=date, bstore=item[4])


        # print(date)

if __name__=='__main__':
    # StudentLoad()
    BookLoad()