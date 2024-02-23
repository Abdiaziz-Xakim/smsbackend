# # urls.py

# from django.urls import path
# from .views import index, StudentView, Student_detail,create_grade
# urlpatterns = [
#     path('api/students/', StudentView.as_view(), name='grade-list-create'),
#     path('api/student/<int:pk>/', Student_detail, name='grade-retrieve-update-destroy'),
#     # Add other URLs as needed
#     path('', index),
#     path('grade/', create_grade, name='create_grade')
# ]


# from django.urls import path
# from .views import ResultListCreateAPIView

# urlpatterns = [
#     path('results/', ResultListCreateAPIView.as_view(), name='result-list-create'),
# ]

from django.urls import path
from django.contrib import admin

from .views import ResultListView

urlpatterns = [
    # path("create/", create_result, name="create-result"),
    # path("edit-results/", edit_results, name="edit-results"),
    path('result/', ResultListView.as_view(), name='view-results'),
]