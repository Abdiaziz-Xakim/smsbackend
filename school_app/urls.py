# from rest_framework import routers
# from .views import StudentsViewSet
# from django.urls import path, include
# from . import views



# router = routers.DefaultRouter()
# # url, views, name 
# router.register('students', StudentsViewSet, 'students')

# urlpatterns = [
#     path('', include(router.urls)),
#     path('register/', views.RegisterStudent.as_view(), name="auth-register"),
# ]

from django.urls import path
from . import views


# urlpatterns = [ 
#     path('students/', views.StudentListView.as_view(), name="student-list"),
#     path('register/', views.RegisterStudent.as_view(), name='register-student'),
#     path('update-student/<int:pk>/', views.UpdateStudentView.as_view(), name='update-student'),
#     path('single-student/<int:pk>/', views.StudentDetailView.as_view(), name='single-student'),
#     path('single-student-by-regno/<int:regno>/', views.StudentDetailViewByRegno.as_view(), name='single-student-by-regno'),

# ]

urlpatterns = [
    path('inactive/', views.InactiveListView.as_view(), name='inactive-student'),
    path('students/', views.StudentListView.as_view(), name='students'),
    path('register/', views.AddStudent.as_view(), name='register'),
    path('single-student/<int:pk>/', views.StudentDetailView.as_view(), name='single-student'),
    path('single-student-by-regno/<int:pk>/', views.StudentDetailView.as_view(), name='single-student-by-regno'),
    path('update-student/<int:pk>/', views.UpdateStudentView.as_view(), name='update-student'),
]