from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.utils import timezone


# Create your models here.
class UserDetails(AbstractUser):
  phone_number = models.CharField(max_length=20, null=True, blank=True)

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  updated_by = models.CharField(max_length=20, null=True, blank=True)

  def save(self, *args, **kwargs):
    self.updated_at = timezone.now()
    super().save(*args, **kwargs)
