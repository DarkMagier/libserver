#!/usr/bin/env python
# -*- coding: utf-8 -*-


def sendhttp():
    import httplib
    import urllib
    import json
    data = urllib.urlencode({'sid': '12345', 'bid':'12345'})
    headers = {"Content-type": "application/x-www-form-urlencoded",
               "Accept": "text/plain"}
    conn = httplib.HTTPConnection(host='=127.0.0.1',port=80)
    conn.request('POST', '/serverapi/queryborrow', data, headers)
    httpres = conn.getresponse()
    data=httpres.read()
    data=json.dumps(json.loads(data),ensure_ascii=False)
    print json.loads(data,encoding='utf-8')
    return data

def studentadd(sid='12345',sname='张扬',smajor='计算机',sclass='信工1班',sphone='12345678912'):
    import httplib
    import urllib
    import json
    data = {'sid':sid, 'sname': sname, 'smajor': smajor, 'sclass': sclass, 'sphone':sphone}
    print data
    headers = {"Content-type": "application/x-www-form-urlencoded",
               "Accept": "text/plain"}
    try:
        conn = httplib.HTTPConnection(host='127.0.0.1', port=80)
        conn.request('POST', '/serverapi/studentadd', data, headers)
        httpres = conn.getresponse()
        result = httpres.read()
        return result.decode()
    except Exception as e:
        print e
    return 'wrong'
studentadd()