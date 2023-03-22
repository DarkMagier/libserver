from django.conf.urls import url
from django.contrib import admin

from Student import views
urlpatterns =[
    url(r'^$',views.student),
    url(r'^addastudent$',views.addastudent),
    url(r'^delastudent',views.delastudent),
    url(r'^allstudent',views.studentall),
    url(r'^delallstudent',views.delallstudent),
    url(r'^queryastudent',views.queryastudent),
    url(r'^editastudent',views.editastudent),
    url(r'^recoverystudent', views.recoverystudent),
        url(r'^backupsstudent', views.backupsstudent),


]
