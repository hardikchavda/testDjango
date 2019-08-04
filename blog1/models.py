from django.db import models

res_choices = [
    ('pass', 'Pass'),
    ('fail', 'Fail'),
    ('absent', 'Absent')
]


class stud(models.Model):
    rno = models.BigAutoField(primary_key=True, verbose_name="Roll Number.")
    rname = models.CharField(max_length=140, verbose_name="Name")
    raddress = models.TextField(null=True, blank=True, verbose_name='Address')
    rujobless = models.BooleanField(default=True, verbose_name="Jobless")

    def __str__(self):
        return self.rname

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Student"


class marks(models.Model):
    srno = models.ForeignKey("stud")
    m1 = models.IntegerField(verbose_name="Django", default=0)
    m2 = models.IntegerField(verbose_name="Ionic", default=0)
    m3 = models.IntegerField(verbose_name="Prog. In R", default=0)
    tot = models.IntegerField(verbose_name="Total", default=0)
    per = models.FloatField(verbose_name="Percentage", default=0.0)
    res = models.CharField(
        max_length=20, choices=res_choices, verbose_name="Result")

    def __str__(self):
        return str(self.srno)

    class Meta:
        verbose_name = "Mark"
        verbose_name_plural = "Marks"
