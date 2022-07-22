from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core.validators import int_list_validator, MinLengthValidator
from django.utils.translation import gettext_lazy as _
# Create your models here.


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""
    def create_user(self, phone, first_name, password=None, **extra_fields):
        """Create , save and return a new user"""
        if not phone:
            raise ValueError('You must provide a phone number')
        user = self.model(phone=phone, first_name=first_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, phone, first_name, password):
        """Create and save a new superuser with given details"""
        user = self.create_user(phone, first_name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class UserProfileModel(AbstractBaseUser, PermissionsMixin):
    """User in the sysetem"""

    first_name = models.CharField(_('first_name'), max_length=30)
    last_name = models.CharField(_('last_name'), max_length=30)
    phone = models.CharField(_('phone number'), max_length=11, unique=True, blank=False,
                             null=False, validators=[MinLengthValidator(11)])
    email = models.EmailField(max_length=40, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_created=True)
    updated_at = models.DateTimeField(auto_now=True)

    last_appointment_datetime = models.DateTimeField(null=True)
    last_appointment_other_user_id = models.IntegerField(null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    objects = UserProfileManager()
    
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['first_name']

    # asign a UserManager

    def __str__(self):
        return f'{self.first_name} , {self.last_name}'
