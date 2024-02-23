# from django.db import models
# from school_app.models import Student

# class Result(models.Model):
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     subject = models.CharField(max_length=100)
#     marks = models.DecimalField(max_digits=5, decimal_places=2)

#     def __str__(self):
#         return f"{self.student.fullname}'s {self.subject} result"

# from django.db import models

# from academics.models import (
#     AcademicSession,
#     AcademicTerm,
#     StudentClass,
#     Subject,
# )
# from school_app.models import Student

# from .utils import score_grade


# # Create your models here.
# class Result(models.Model):
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     session = models.ForeignKey(AcademicSession, on_delete=models.CASCADE)
#     term = models.ForeignKey(AcademicTerm, on_delete=models.CASCADE)
#     current_class = models.ForeignKey(StudentClass, on_delete=models.CASCADE)
#     subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
#     test_score = models.IntegerField(default=0)
#     exam_score = models.IntegerField(default=0)

#     class Meta:
#         ordering = ["subject"]

#     def __str__(self):
#         return f"{self.student} {self.session} {self.term} {self.subject}"

#     def total_score(self):
#         return self.test_score + self.exam_score

#     def grade(self):
#         return score_grade(self.total_score())

from django.db import models

from academics.models import AcademicYear, AcademicTerm, StudentClass, Subject
from school_app.models import Student
from .utils import score_grade


class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    session = models.ForeignKey(AcademicYear, on_delete=models.CASCADE)
    term = models.ForeignKey(AcademicTerm, on_delete=models.CASCADE)
    current_class = models.ForeignKey(StudentClass, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("student", "session", "term", "current_class")


class SubjectResult(models.Model):
    result = models.ForeignKey(Result, on_delete=models.CASCADE, related_name='subject_results')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    test_score = models.IntegerField(default=0)
    exam_score = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.result.student} - {self.subject.name}"

    def total_score(self):
        return self.test_score + self.exam_score

    def grade(self):
        return score_grade(self.total_score())