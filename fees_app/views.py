# fees_app/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Feepayment
from .serializers import FeePaymentSerializer
from rest_framework import viewsets, permissions
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import generics

    
class CustomPageNumberPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


# class FeepaymentViewSet(viewsets.ModelViewSet):
#     queryset = Feepayment.objects.filter(is_active=True).order_by('-id')
#     serializer_class = FeePaymentSerializer
#     permission_classes = [ permissions.AllowAny ]
#     pagination_class = CustomPageNumberPagination

#     filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
#     filterset_fields = ['regno', 'fullname', 'payment_date', 'amount']
#     search_fields = ['regno', 'fullname', 'payment_date', 'amount']
#     ordering_fields = ['regno', 'fullname', 'payment_date', 'amount']


class FeepaymentView(generics.ListAPIView):
    queryset = Feepayment.objects.filter(is_active=True).order_by('-id')
    permission_classes = [ permissions.AllowAny ] 
    serializer_class = FeePaymentSerializer
    pagination_class = CustomPageNumberPagination

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['regno', 'fullname', 'payment_date', 'amount']
    search_fields = ['regno', 'fullname', 'payment_date', 'amount']
    ordering_fields = ['regno', 'fullname', 'payment_date', 'amount']

# fee detail
class FeePaymentDetailView(generics.RetrieveAPIView):
    permission_classes = [
        permissions.AllowAny,
    ] 

    queryset = Feepayment.objects.all()

    serializer_class = FeePaymentSerializer

# update fee
class UpdateFeePaymentView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Feepayment.objects.all()
    serializer_class = FeePaymentSerializer
    permission_classes = [permissions.AllowAny,]

    def put(self, request, *args, **kwargs):
        return super().put(request,*args, **kwargs)
    
# add fee
class AddFeePayment(generics.GenericAPIView):
    permission_classes = [
        permissions.AllowAny,
    ] 

    serializer_class = FeePaymentSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        fee = serializer.save()

        return Response({
            "fee": FeePaymentSerializer(fee,
            context=self.get_serializer_context()).data, 
        })
