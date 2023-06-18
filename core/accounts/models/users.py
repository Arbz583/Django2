from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser, PermissionsMixin)


class UserManager(BaseUserManager):
    '''
    custom model user manager where emaiml is the unique identifiers for authentiacation instead of usernames.
    '''
    def create_user(self, email, password, **extra_fields):
        """
        Creates and saves a user with the given email and password and extra data
        """       
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user    

    def create_superuser(self, email, password, **extra_fields):
        """
        Creates and saves a superuser with the given email and password and extra data
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    '''
    custom model use for our app
    '''
    email=models.EmailField(max_length=255, unique=True)
    is_superuser=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    #is_verified=models.BooleanField(default=False)
    #first_name=models.CharField(max_length=20)

    USERNAME_FIELD = 'email'
    #REQUIRED_FIELDS = ['first_name']          #must be fill when it'll be created

    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)

    objects=UserManager()

    def __str__(self):
        return(self.email)