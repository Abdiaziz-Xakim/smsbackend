# fees_app/models.py
from django.db import models
from school_app.models import Student
from django.utils import timezone

# Create your models here.
class Feepayment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, default=1)
    regno = models.CharField(max_length=100, default='')
    fullname = models.CharField(max_length=100, default='')
    payment_date = models.CharField(max_length=100, blank=True) 
    amount = models.CharField(max_length=100, default=1)
    date_reg = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.regno
    