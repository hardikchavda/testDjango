from django.db import models

class studInfo(models.Model):
    rno = models.IntegerField(primary_key=True)
    rname = models.CharField(max_length=150)
    raddress = models.CharField( max_length=255)

    def __str__(self):
        return self.rname
    
