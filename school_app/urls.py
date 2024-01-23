from rest_framework import routers
from .views import StudentsViewSet
from django.urls import path, include
from . import views



router = routers.DefaultRouter()
# url, views, name 
router.register('students', StudentsViewSet, 'students')

urlpatterns = [
    path('', include(router.urls)),
    path('register/', views.RegisterStudent.as_view(), name="auth-register"),
]