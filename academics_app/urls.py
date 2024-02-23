from django.urls import path
from . import views

urlpatterns = [
    path('subjects/', views.SubjectListCreate.as_view(), name='subject-list-create'),
    path('subjects/<int:pk>/', views.SubjectRetrieveUpdateDestroy.as_view(), name='subject-detail'),
    path('result/', views.ResultListCreate.as_view(), name='result-list-create'),
    path('results/<int:pk>/', views.ResultRetrieveUpdateDestroy.as_view(), name='result-detail'),
]