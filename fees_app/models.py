# fees_app/models.py
from django.db import models
from school_app.models import Student
from django.utils import timezone

# Create your models here.
class Feepayment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, default=1)
    amount = models.CharField(max_length=100, default=1)
    payment_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.amount
    