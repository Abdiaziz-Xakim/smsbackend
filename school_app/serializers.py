from .models import Student
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'regno', 'fullname', 'classs', 'parents_name', 'parents_contact', 'fees', 'is_active']

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'regno', 'fullname', 'classs', 'parents_name', 'parents_contact', 'fees']
        # extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        student = Student.objects.create_student(
            validated_data['regno'],
            validated_data['fullname'],
            validated_data['parents_name'],
            validated_data['parents_contact'],
            validated_data['fees'],
        )
            
        return student