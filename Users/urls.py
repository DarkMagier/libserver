from django.conf.urls import url
from Users import views
urlpatterns=[
    url(r'^$',views.login),
    url(r'^signup',views.signup),
    url(r'^logout',views.logout)

]