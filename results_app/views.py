from rest_framework import generics
from rest_framework.response import Response
from .serializers import ResultSerializer, SubjectResultSerializer
from .models import Result, SubjectResult

class ResultListView(generics.ListAPIView):
    serializer_class = ResultSerializer

    def get_queryset(self):
        return Result.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

class SubjectResultListView(generics.ListAPIView):
    serializer_class = SubjectResultSerializer

    def get_queryset(self):
        return SubjectResult.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
