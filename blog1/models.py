from django.db import models

class studInfo(models.Model):
    rno = models.IntegerField(primary_key=True)
    rname = models.CharField(max_length=150)
    raddress = models.CharField( max_length=255)
    rphone = models.IntegerField(null=True)

    def __str__(self):
        return self.rname

    class Meta:
        verbose_name = "Student Information"
        verbose_name_plural = "Student's Information"
    
 
class studResult(models.Model):
    sInfo = models.ForeignKey("studInfo")
    django = models.IntegerField(null=False)
    progR = models.IntegerField(null=False)
    ionic = models.IntegerField(null=False)
    total = models.IntegerField(null=False)
    per = models.FloatField(null=False)

    def __str__(self):
        return str(self.sInfo)

    class Meta:
        verbose_name = "Student Result"
        verbose_name_plural = "Student's Result"
