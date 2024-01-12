from django.db import models
from django.utils import timezone

# Create your models here.
class Student(models.Model):
    regno = models.CharField(max_length=100)
    fullname = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    contact = models.CharField(max_length=100, default=1)
    date_reg = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.regno
    
    
    
    
 