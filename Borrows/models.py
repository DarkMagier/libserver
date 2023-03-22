from django.db import models
from Student import models as sm
from Books import models as bm


# Create your models here.

class BorrowInfo(models.Model):
    bwid=models.CharField(max_length=12,unique=True,primary_key=True)
    sid = models.ForeignKey(sm.StudentInfo,null=False,related_name='student')
    bid = models.ForeignKey(bm.BookInfo,null=False,related_name='book')
    bdate = models.DateField(auto_created=True,auto_now_add=True)
