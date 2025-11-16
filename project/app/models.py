# Create your models here.
from django.db import models

class student(models.Model):
  
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=15, null=True)
    details = models.TextField(blank=True, null=True)


    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES,  null=True)

   
    qualification = models.JSONField( null=True)  
   
   
    EDUCATION_CHOICES = [
        ('bsc', 'B.Sc'),
        ('ba', 'B.A'),
        ('btech', 'B.Tech'),
        ('msc', 'M.Sc'),
        ('ma', 'M.A'),
        ('mtech', 'M.Tech'),
        ('mba', 'MBA'),
        ('phd', 'PhD'),
    ]
    education = models.CharField(max_length=10, choices=EDUCATION_CHOICES, blank=True, null=True)

    # File uploads
    profile_pic = models.ImageField(upload_to='uploads/images/', blank=True, null=True)
    document = models.FileField(upload_to='uploads/docs/', blank=True, null=True)
    audio = models.FileField(upload_to='uploads/audios/', blank=True, null=True)
    video = models.FileField(upload_to='uploads/videos/', blank=True, null=True)
    password=models.CharField(max_length=50,null=True)
   

    def str(self):
        return self.name