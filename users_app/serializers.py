from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

User=get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'mobile', 'location', 'role', 'date_joined', 'is_active')


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'mobile', 'location', 'role', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['email'],
            validated_data['password'],
            validated_data['first_name'],
            validated_data['last_name'],
            validated_data['mobile'],
            validated_data['location'],
            validated_data['role']
        )
            
        return user
    
# Login Serializer
class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()
    
    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")
    

# Change password serialzer

class ChangePasswordSerializer(serializers.Serializer):
    model = User

    currentPassword = serializers.CharField(required=True)
    newPassword = serializers.CharField(required=True)