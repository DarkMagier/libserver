from django.db import models

# Create your models here.
class UserInfo(models.Model):
    username=models.CharField(max_length=15,unique=True,primary_key=True,verbose_name='账号')
    password=models.CharField(max_length=15,verbose_name='密码')
