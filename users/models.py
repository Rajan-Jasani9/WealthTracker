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


class UserToken(models.Model):
  """
  Model representing a user token.

  Inherits from the CommonInfo abstract base model for common fields.
  """

  user = models.ForeignKey(UserDetails,
                           related_name="user",
                           on_delete=models.CASCADE,
                           null=True,
                           blank=True,
                           db_index=True)
  token = models.CharField(null=True, blank=True, max_length=500)

  def __str__(self):
    return str(self.user) + ' - UserTokenID - ' + str(self.id)

  class Meta:
    db_table = "user_tokens"
