from rest_framework import serializers

from school_app.models import Student
from .models import Result, SubjectResult

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class SubjectResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectResult
        fields = '__all__'

class ResultSerializer(serializers.ModelSerializer):
    student = StudentSerializer()
    subject_results = SubjectResultSerializer(many=True)

    class Meta:
        model = Result
        fields = '__all__'
