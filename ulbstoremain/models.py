from django.db import models
from django.utils import timezone
import datetime

#Create deparment
class Department(models.Model):
    STORE_DEPFLAG = (
        ('y','Yes'),
        ('n','No')
    )
    STATUS_DEPFLAG = (
        ('a','Active'),
        ('i','Inactive')
    )

    depcode = models.CharField(max_length = 250)
    depdescription = models.CharField(max_length = 250)
    store_depflag = models.CharField(max_length = 10, choices = STORE_DEPFLAG, default='y')
    status = models.CharField(max_length = 10, choices = STATUS_DEPFLAG, default='a')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-depcode',)
    
    def __str__(self):
        return self.depdescription



#Create financialyear
class Financialyear(models.Model):
    STATUS_DEPFLAG = (
        ('a','Active'),
        ('i','Inactive')
    )

    fafromdate = models.DateField(default=datetime.date.today)
    fatodate =models.DateField(default=datetime.date.today)
    status = models.CharField(max_length = 10, choices = STATUS_DEPFLAG, default='a')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-fafromdate',)
    
    def __str__(self):
        return str(self.fafromdate)




