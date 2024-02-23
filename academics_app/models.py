from django.db import models

from school_app.models import Student

class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='results')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateField()

    class Meta:
        ordering = ['student', 'date']

    def __str__(self):
        return f"{self.student} - {self.subject.name}"