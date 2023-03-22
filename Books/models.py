from django.db import models

# Create your models here.

class BookInfo(models.Model):
    bid     =models.CharField(max_length=15,unique=True,primary_key=True,verbose_name='书号')
    bname       =models.CharField(max_length=64,verbose_name='书名')
    bauthor     =models.CharField(max_length=64,verbose_name='作者')
    bpublisher      =models.CharField(max_length=64,verbose_name='出版社')
    bdate       =models.DateField(verbose_name='出版日期')
    bstore      =models.IntegerField(verbose_name='库存')
    bborrow     =models.IntegerField(verbose_name='借阅量',default=0)

    def natural_key(self):
        return {'bid':self.bid, 'bname':self.bname,'bauthor':self.bauthor,'bpublisher':self.bpublisher,'bdate':self.bdate,'bstore':self.bstore,'bborrow':self.bborrow}

    class Meta:
        unique_together = (('bid', 'bname','bauthor','bpublisher','bdate','bstore','bborrow'),)