# fees_app/urls.py
from django.urls import path
from rest_framework import routers
from django.urls import path, include
from rest_framework.response import Response
from .views import FeepaymentView, UpdateFeePaymentView, FeePaymentDetailView, AddFeePayment


# router = routers.DefaultRouter()
# router.register('feepayments', FeepaymentViewSet, 'feepayments')


urlpatterns = [
#  path('', include(router.urls)),
   path('feepayments/', FeepaymentView.as_view(), name='feepayments'),
   path('update-fee/<int:pk>/', UpdateFeePaymentView.as_view(), name='update-feepayment'),
   path('fee-detail/<int:pk>/', FeePaymentDetailView.as_view(), name='fee-detail'),
   path('add-fee/', AddFeePayment.as_view(), name="add-feepayment"),
]