from rest_framework import serializers
from .models import Subject, Result
from school_app.models import Student  # Assuming you also need a serializer for the Student model

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'name']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name']  # Adjust fields according to your Student model

class ResultSerializer(serializers.ModelSerializer):
    student = StudentSerializer(read_only=True)
    subject = SubjectSerializer(read_only=True)

    class Meta:
        model = Result
        fields = ['id', 'student', 'subject', 'score', 'date']
        depth = 1  # Optional: Adjust this if you need more detailed nested serialization

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name']  # Adjust fields according to your Student model

class ResultSerializer(serializers.ModelSerializer):
    student = StudentSerializer(read_only=True)
    subject = SubjectSerializer(read_only=True)

    class Meta:
        model = Result
        fields = ['id', 'student', 'subject', 'score', 'date']
        depth = 1  # Optional: Adjust this if you need more detailed nested serialization

class ResultSerializer(serializers.ModelSerializer):
    student = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all())
    subject = serializers.PrimaryKeyRelatedField(queryset=Subject.objects.all())

    class Meta:
        model = Result
        fields = ['id', 'student', 'subject', 'score', 'date']
