from django.db import models
from django.forms import Textarea
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
    suppliercode = models.CharField(max_length = 10, verbose_name ='Supplier Code')
    suppliername = models.CharField(max_length = 200, blank=True, null=True, verbose_name ='Suplier Name')
    supplieraddress = models.TextField(verbose_name ='Suplier Address')
    suppliertelephone = models.CharField(max_length = 15, blank=True, null=True, verbose_name ='Suplier Telephone')
    suppliermobileno = models.CharField(max_length = 10, blank=True, null=True, verbose_name ='Mobile Number')
    supplieremailid = models.EmailField(max_length = 100, blank=True, null=True, verbose_name ='e-mail')
    vatno = models.CharField(max_length = 25, blank=True, null=True, verbose_name ='VAT No')
    cstno = models.CharField(max_length = 25, blank=True, null=True, verbose_name ='CST No')
    tinno = models.CharField(max_length = 25, blank=True, null=True, verbose_name ='Tin No.')
    status = models.CharField(max_length = 10, choices = STATUS_SUPFLAG, default='a')
    created = models.DateTimeField(auto_now_add=True, blank=True),
    updated = models.DateTimeField(auto_now_add=True, blank=True),

    class Meta:
        ordering = ('suppliername',)
    
    def __str__(self):
        return self.suppliername
