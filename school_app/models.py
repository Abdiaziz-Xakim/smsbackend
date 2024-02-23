from django.db import models
from django.utils import timezone

# Create your models here.
class Student(models.Model):
    regno = models.IntegerField()
    fullname = models.CharField(max_length=100)
    classs= models.CharField(max_length=100, default=1)
    parents_name = models.CharField(max_length=100, default='')
    parents_contact = models.CharField(max_length=100, blank=True, null=True)
    fees= models.CharField(max_length=100)
    # email = models.CharField(max_length=100, unique=True)
    # contact = models.CharField(max_length=100, default=1)
    date_reg = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.fullname}"