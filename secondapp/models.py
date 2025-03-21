from django.db import models

# Create your models here.
class DepartmentModel(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    description=models.TextField(null=True,blank=True)

    def __str__(self):
        return self.name

class GalleryModel(models.Model):
    name=models.CharField(max_length=20,null=True,blank=True)
    galimage=models.ImageField(null=True, blank=True,upload_to='gallery')


class FacilitiesModel(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    fac_image = models.ImageField(null=True, blank=True, upload_to='facilities')


    def __str__(self):
        return self.name

class  DoctorsModel(models.Model):
    department=models.ForeignKey(DepartmentModel,on_delete=models.CASCADE,null=True,blank=True,related_name='doctors')
    name=models.CharField(max_length=50,null=True,blank=True)
    qualification=models.CharField(max_length=100,null=True,blank=True)
    experience=models.CharField(max_length=100,null=True,blank=True)
    op=models.CharField(max_length=50,null=True,blank=True)
    doctor_image = models.ImageField(null=True, blank=True, upload_to='doctors')

    def __str__(self):
        return self.name

class BookingModel(models.Model):
    patient_name=models.CharField(max_length=50,null=True,blank=True)
    patient_phone=models.CharField(max_length=11,null=True,blank=True)
    patient_email=models.EmailField(null=True,blank=True)
    doctor_name=models.CharField(max_length=50,null=True,blank=True)
    booking_date=models.DateField(null=True,blank=True)

    def __str__(self):
        return self.patient_name

class CareersModel(models.Model):
    job_title=models.CharField(max_length=50,null=True,blank=True)
    JOBTYPE = [
        ('all', 'All'),
        ('full time', 'Full time'),
    ]
    job_type = models.CharField(max_length=255, choices=JOBTYPE, default='all')
    JOBWORKSPACE = [
        ('all', 'All'),
        ('in office', 'In Office'),
    ]
    job_workspace = models.CharField(max_length=255, choices=JOBWORKSPACE, default='all')
    job_desc=models.TextField(null=True,blank=True)
    job_req=models.TextField(null=True,blank=True)

    def __str__(self):
        return self.job_title

class Person(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name


