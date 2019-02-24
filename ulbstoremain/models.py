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

#Create supplier
class Supplier(models.Model):
    STATUS_SUPFLAG = (
        ('A','Active'),
        ('I','Inactvie')
    )
    suppliercode = models.CharField(max_length = 10)
    suppliername = models.CharField(max_length = 200, blank=True, null=True)
    supplieraddress = models.CharField(max_length = 500, blank=True, null=True)
    suppliertelephone = models.CharField(max_length = 15, blank=True, null=True)
    suppliermobileno = models.CharField(max_length = 10, blank=True, null=True)
    supplieremailid = models.CharField(max_length = 100, blank=True, null=True)
    vatno = models.CharField(max_length = 25, blank=True, null=True)
    cstno = models.CharField(max_length = 25, blank=True, null=True)
    tinno = models.CharField(max_length = 25, blank=True, null=True)
    status = models.CharField(max_length = 10, choices = STATUS_SUPFLAG, default='a')
    created = models.DateTimeField(auto_now_add=True, blank=True),
    updated = models.DateTimeField(auto_now_add=True, blank=True),

    class Meta:
        ordering = ('suppliername',)
    
    def __str__(self):
        return self.suppliername
