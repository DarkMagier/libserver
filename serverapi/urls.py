from django.conf.urls import url
from django.contrib import admin

from serverapi import views
urlpatterns =[
    url(r'^$',views.home),
    url(r'test',views.test),
    url(r'^studentall$',views.studentall),
    url(r'^studentquery',views.studentquery),
    url(r'^studentadd',views.studentadd),
    url(r'^studentdel',views.studentdel),
    url(r'^studentedit',views.studentedit),
    url(r'^studentDelAll',views.studentDelAll),
    url(r'^recoverystudent', views.recoverystudent),
    url(r'^backupsstudent', views.backupsstudent),


    url(r'^bookall$', views.bookall),
    url(r'^bookquery', views.bookquery),
    url(r'^bookadd', views.bookadd),
    url(r'^bookdel', views.bookdel),
    url(r'^bookedit', views.bookedit),
    url(r'^bookDelAll', views.bookDelAll),
    url(r'^backupsbook', views.backupsbook),
    url(r'^recoverybook', views.recoverybook),


    url(r'^borrowbooks', views.borrowbooks),
    url(r'^returnbooks', views.returnbooks),
    url(r'^allborrows', views.allborrows),
    url(r'^queryborrow', views.queryborrow),
    url(r'^recoveryborrow', views.recoveryborrow),
    url(r'^backupsborrow', views.backupsborrow),
    url(r'^signup', views.signup),
    url(r'^logout', views.logout),
    url(r'^login', views.login),





]
