# from django.shortcuts import render
# from rest_framework import viewsets, permissions
# from .models import Student
# from .serializers import StudentSerializer
# from rest_framework.pagination import PageNumberPagination

# from .serializers import StudentSerializer, RegisterSerializer
# from rest_framework import filters, permissions, generics
# from .serializers import StudentSerializerc
# from rest_framework.response import Response



# # Create your views here.

# # PAGINATION CLASS

# class CustomPageNumberPagination(PageNumberPagination):
#     page_size = 10
#     page_size_query_param = 'page_size'
#     max_page_size = 100


# class StudentsViewSet(viewsets.ModelViewSet):
#     queryset = Student.objects.filter(is_active=True).order_by('id')
#     # queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     permission_classes = [ permissions.AllowAny ]
#     pagination_class = CustomPageNumberPagination


#     # Regster Student view
# class RegisterStudent(generics.GenericAPIView):
#     permission_classes = [
#         permissions.AllowAny,
#     ] 

#     serializer_class = StudentSerializer
    
#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         student = serializer.save()
        
#         return Response({
#             "student": StudentSerializer(student,
#             context=self.get_serializer_context()).data, 
#         })

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters, permissions, generics
from .serializers import StudentSerializer, RegisterSerializer
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer, RegisterSerializer

import datetime, random, string
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import render


class CustomPageNumberPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class StudentListView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [ permissions.AllowAny ] 
    pagination_class = CustomPageNumberPagination

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['regno', 'fullname', 'classs', 'parents_name', 'parents_contact', 'fees']
    search_fields = ['regno', 'fullname', 'classs', 'parents_name', 'parents_contact', 'fees']
    ordering_fields = ['regno', 'fullname', 'classs', 'parents_name', 'parents_contact', 'fees']

# Detail view
class StudentDetailView(generics.RetrieveAPIView):
    permission_classes = [
        permissions.AllowAny,
    ] 

    queryset = Student.objects.all()
    
    serializer_class = StudentSerializer
    
# Regster user view
class RegisterStudent(generics.GenericAPIView):
    permission_classes = [
        permissions.AllowAny,
    ] 

    serializer_class = RegisterSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        student = serializer.save()
        
        return Response({
            "student": StudentSerializer(student,
            context=self.get_serializer_context()).data, 
        })
    
# Update user
class UpdateStudentView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.AllowAny,]

    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)