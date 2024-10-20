

# Create your models here.
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)  # Email field is required

    # Add related_name to avoid conflicts with default User model
    groups = models.ManyToManyField(
        Group, related_name="customuser_set", blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission, related_name="customuser_permissions_set", blank=True
    )

    def __str__(self):
        return self.username  # Optional, defines a string representation for the user

    class Meta:
        permissions = [
            # Add any custom permissions here if needed
        ]