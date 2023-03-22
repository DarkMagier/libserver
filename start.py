import socket
import os
ip_addrList=socket.gethostbyname_ex(socket.gethostname())[2]
ip_addr="192.168.1.101"
ip_port="8000"
for ip in ip_addrList:
    if ip.startswith('10.1'):
        ip_addr=ip
print (ip_addr)
os.system("C:\Users\J\AppData\Local\Programs\Python\Python36\python.exe manage.py runserver %s:%s"%(ip_addr,ip_port))

