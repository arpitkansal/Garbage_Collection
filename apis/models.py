from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Vehicle(models.Model):
    vehicle_no = models.CharField(max_length=15,unique=True)
    model = models.CharField(max_length= 20 , null = True,blank=True)
    gps_chip = models.CharField(max_length=20, null = True,blank=True)
    lats = models.DecimalField(decimal_places=8,max_digits=11)
    longs = models.DecimalField(decimal_places=8,max_digits=11)


class Driver(models.Model):
    driver_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name="vehicle")
    def __str__(self):
        return self.name


class Area(models.Model):
    area_id = models.CharField(max_length= 20 ,unique=True)
    name = models.CharField(max_length=20,null=True)
    lats = models.DecimalField(decimal_places=8,max_digits=11)
    longs = models.DecimalField(decimal_places=8,max_digits=11)
    radius = models.DecimalField(decimal_places=2,max_digits=4)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name="driver", null=True)
    def __str__(self):
        return self.name

class Complaint(models.Model):
    complaint_id = models.AutoField(primary_key=True)
    details = models.TextField(max_length= 300 )
    created_date = models.DateField()
    disposed_date = models.DateField()
    area = models.ForeignKey(Area, on_delete=models.CASCADE, related_name="complaint_area")
    def __str__(self):
        return self.complaint_id

class Residents(models.Model):
    res_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    area = models.ForeignKey(Area, on_delete=models.CASCADE, related_name="resident_area")
    complaint = models.ForeignKey(Complaint, on_delete=models.CASCADE, blank = True, null = True)
    def __str__(self):
        return self.name