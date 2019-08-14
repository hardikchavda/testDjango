from django.db import models

city = [
    ('rkt','Rajkot'),
    ('amd','Ahemedabad'),
    ('sur','Surat')
    ]

class studInfo(models.Model):
    rno = models.AutoField(primary_key=True,verbose_name="Roll Number.")
    rname = models.CharField(max_length=150, verbose_name="Student Name")
    raddress = models.CharField( max_length=255, verbose_name="Address")
    rcity = models.CharField(default="Rajkot",choices=city,max_length=50,verbose_name="City")
    rphone = models.IntegerField(blank=True,null=True,verbose_name="Contact Number")

    def __str__(self):
        return self.rname

    class Meta:
        verbose_name = "Student Information"
        verbose_name_plural = "Student's Information"
    
 
class studResult(models.Model):
    sInfo =  models.ForeignKey("studInfo",  on_delete=models.CASCADE)
    django = models.IntegerField(null=False)
    progR = models.IntegerField(null=False)
    ionic = models.IntegerField(null=False)
    total = models.IntegerField(null=False)
    per = models.FloatField(null=False)

    def __str__(self):
        return str(self.sInfo)

    class Meta:
        verbose_name = "Student's Result"
        verbose_name_plural = "Student's Result"
