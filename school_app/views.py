from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Student
from .serializers import StudentSerializer
from rest_framework.pagination import PageNumberPagination


# Create your views here.

# PAGINATION CLASS

class CustomPageNumberPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class StudentsViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.filter(is_active=True).order_by('id')
    # queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [ permissions.AllowAny ]
    pagination_class = CustomPageNumberPagination