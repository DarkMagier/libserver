import http.client
import urllib
import json
import requests
def getStudentAll():

    url = """http://localhost:8000/serverapi/studentall"""

    response=requests.get(url)
    data=json.loads(response.content)
    # print(data)
    stuList=[]
    for item in data:
        stu={}
        stu['sid']=item['pk']
        for (k,v) in item['fields'].items():
            stu[k]=v
        stuList.append(stu)
    return stuList
def studentquery():
    data={'sid':'12345'}
    url="""http://localhost:8000/serverapi/studentquery"""
    response=requests.post(url,data)
    data=json.loads(response.content)
    stuList = []
    for item in data:
        stu = {}
        stu['sid'] = item['pk']
        for (k, v) in item['fields'].items():
            stu[k] = v
        stuList.append(stu)
    return stuList
def studentadd(sid='12345',sname='张扬',smajor='计算机',sclass='信工1班',sphone='12345678912'):
    data = {'sid':sid, 'sname': sname, 'smajor': smajor, 'sclass': sclass, 'sphone':sphone}
    url = """http://localhost:8000/serverapi/studentadd"""
    response = requests.post(url, data)
    data=response.content
    return data.decode()
def studentdel():
    data = {'sid': '123456', }
    url = """http://localhost:8000/serverapi/studentdel"""
    response = requests.post(url, data)
    data=response.content
    return data.decode()
def studentedit():
    data = {'sid': '123456', 'sname': '张扬aa', 'smajor': '计算机', 'sclass': '信工1班', 'sphone': '12345678921'}
    url = """http://localhost:8000/serverapi/studentedit"""
    response = requests.post(url, data)
    data=response.content
    return data.decode()
def studentDelAll():
    url = """http://localhost:8000/serverapi/studentDelAll"""
    response = requests.post(url)
    data = response.content
    return data.decode()
def getbookAll():
    url = """http://localhost:8000/serverapi/bookall"""

    response=requests.get(url)
    data=json.loads(response.content)
    # print(data)
    bkList=[]
    for item in data:
        stu={}
        stu['bid']=item['pk']
        for (k,v) in item['fields'].items():
            stu[k]=v
        bkList.append(stu)
    return bkList
def bookquery():
    data={'bid':'12345'}
    url="""http://localhost:8000/serverapi/bookquery"""
    response=requests.post(url,data)
    data=json.loads(response.content)
    bkList = []
    for item in data:
        stu = {}
        stu['bid'] = item['pk']
        for (k, v) in item['fields'].items():
            stu[k] = v
        bkList.append(stu)
    return bkList
def bookadd(bid='12345',bname='MySQL从删库到跑路',bauthor='Django从入门到放弃',bpublisher='Python人工不智能之路',bdate='1927-2-3',bstore=2):
    data = {'bid':bid, 'bname': bname, 'bauthor': bauthor, 'bpublisher': bpublisher, 'bdate':bdate,'bstore':bstore}
    url = """http://localhost:8000/serverapi/bookadd"""
    response = requests.post(url, data)
    data=response.content
    return data.decode()
def bookdel():
    data = {'bid': '12345', }
    url = """http://localhost:8000/serverapi/bookdel"""
    response = requests.post(url, data)
    data=response.content
    return data.decode()
def bookedit():
    data = {'bid': '12345', 'bname': 'MySQL从删库到跑路2', 'bauthor': 'Django从入门到放弃', 'bpublisher': 'Python人工不智能之路',
            'bdate': '1927-2-3', 'bstore': 2}
    url = """http://localhost:8000/serverapi/bookedit"""
    response = requests.post(url, data)
    data=response.content
    return data.decode()
def bookDelAll():
    url = """http://localhost:8000/serverapi/bookDelAll"""
    response = requests.post(url)
    data = response.content
    return data.decode()

def borrowbooks():
    data = {'sid': '12345','bid':'12345' }
    url = """http://localhost:8000/serverapi/borrowbooks"""
    response = requests.post(url, data)
    data = response.content
    return data.decode()
def returnbooks():
    data = {'sid': '12345','bid':'12345' }
    url = """http://localhost:8000/serverapi/returnbooks"""
    response = requests.post(url, data)
    data = response.content
    return data.decode()
def allborrows():
    url = """http://localhost:8000/serverapi/allborrows"""
    response = requests.get(url)
    data = response.content
    data = json.loads(data)
    return data
def queryborrow():
    data = {'sid': '12345','bid':'12345' }
    url = """http://localhost:8000/serverapi/queryborrow"""
    response = requests.post(url, data)
    data = response.content
    data = json.loads(data)
    return data

if __name__=='__main__':
    stuList=getStudentAll()
    # stuList = studentquery()
    # stuListadd = studentadd()
    # stuList = studentdel()
    # stuListedi = studentedit()
    # stuList = studentDelAll()
    # print(stuListadd)
    # print(stuList)
    # res=bookadd()
    # res=bookdel()
    # res=bookedit()
    # res=bookquery()
    # res=getbookAll()
    # res=bookDelAll()
    # res=borrowbooks()
    # res=returnbooks()
    # res=allborrows()
    res=queryborrow()
    print(res)
