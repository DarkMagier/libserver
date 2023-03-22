from django.db import models

class StudentInfo(models.Model):
    sid = models.CharField(max_length=15,unique=True,primary_key=True,verbose_name='学号')
    sname = models.CharField(max_length=15,verbose_name='姓名')
    smajor = models.CharField(max_length=15,verbose_name='专业')
    sclass = models.CharField(max_length=15,verbose_name='班级')
    sphone= models.CharField(max_length=15,verbose_name='手机号')

    def natural_key(self):
        return {'sid':self.sid, 'sname':self.sname,'smajor':self.smajor,'sclass':self.sclass,'sphone':self.sphone,}

    class Meta:
        unique_together = (('sid', 'sname','smajor','sclass','sphone'),)




