from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone


class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, first_name, last_name, mobile, location, role, **extra_fields):
        if not email:
            raise ValueError('The Email must be set')
        if not password:
            raise ValueError('The password must be set')

        user = self.model(
            email = self.normalize_email(email),
            first_name=first_name, 
            last_name=last_name, 
            mobile=mobile, 
            location=location, 
            role=role, 
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, first_name, last_name, mobile, location, role, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_active', True)
        return self._create_user(email, password, first_name, last_name, mobile, location, role, **extra_fields)

    def create_superuser(self, email, password, first_name, last_name, mobile, location, role, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        return self._create_user(email, password, first_name, last_name, mobile, location, role, **extra_fields)
    
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(db_index=True, blank=True, unique=True, max_length=254)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    mobile = models.CharField(max_length=50, blank=True)
    location = models.CharField(max_length=255, default='')
    role = models.CharField(max_length=255, default='')
    date_joined = models.DateTimeField(default=timezone.now)

    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'mobile', 'location', 'role']

    objects =CustomUserManager()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.email
    
# Storing Password

class PasswordReset(models.Model):
    email = models.EmailField(max_length=254)
    token = models.CharField(max_length=254, unique=True)
    date_created = models.DateTimeField(default=timezone.now)
    status = models.EmailField(max_length=254, default='')