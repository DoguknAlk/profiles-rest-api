from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('User must have email adress')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name) 

        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, name, password):
        """Create and save a new superuser with given details"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in system"""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()


    USERNAME_FIELD = 'email'    
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retreive full name of user"""
        return self.name 

    def get_short_name(self):
        """Retreive short name of user"""
        return self.name

    def __str__(self):
        """Return string representation of our user"""
        return self.email

class ProfileFeedItem(models.Model): #Main class for items
    """Profile status update"""
    user_profile = models.ForeignKey( #We use foreignKey to associate the item with UserProfile
        settings.AUTH_USER_MODEL, # we need to use this so that If there is a change in UserProfile we will not need to change it manually.
        on_delete=models.CASCADE # If the profile associated to item removed, remove the item. 
    )
    status_text = models.CharField(max_length=255) 
    created_on = models.DateTimeField(auto_now_add=True) #When an Item created automatically add time stant when It is created
    def __str__(self):
        """Return the model as a string"""
        return self.status_text

    # After typing this we have to migrate the data.
    # In git, after we activate virtual environment, we should write:
    # "python manage.py makemigrations"
    # After this new migration file should be created. To apply write:
    # "python manage.py migrate"

    # Next register to admin by going admin.py
