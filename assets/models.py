from collections import defaultdict
from django.db import models
from django.utils import timezone


# enums
class AssetType(models.TextChoices):
  STOCK = "STOCK", "Stock"
  BOND = "BOND", "Bond"
  REAL_ESTATE = "REAL_ESTATE", "Real Estate"
  CASH = "CASH", "Cash"
  CRYPTO = "CRYPTO", "Cryptocurrency"
  MUTUAL_FUND = "MUTUAL_FUND", "Mutual Fund"
  ETF = "ETF", "Exchange-Traded Fund"
  COMMODITY = "COMMODITY", "Commodity"
  PRECIOUS_METAL = "PRECIOUS_METAL", "Precious Metal"
  ART = "ART", "Art"
  COLLECTIBLE = "COLLECTIBLE", "Collectible"
  VEHICLE = "VEHICLE", "Vehicle"
  BUSINESS = "BUSINESS", "Business"
  OTHER = "OTHER", "Other"


class AssetStatus(models.TextChoices):
  ACTIVE = "ACTIVE", "Active"
  INACTIVE = "INACTIVE", "Inactive"


# Create your models here.
class Asset(models.Model):
  name = models.CharField(max_length=255)
  description = models.TextField(max_length=255, blank=True)
  asset_type = models.CharField(
      max_length=50,
      choices=AssetType.choices,
      default=AssetType.OTHER,
  )
  asset_status = models.CharField(
      max_length=50,
      choices=AssetStatus.choices,
      default=AssetStatus.ACTIVE,
  )
  purchase_cost = models.DecimalField(max_digits=12, decimal_places=2)
  purchase_date = models.DateField(null=True)
  value = models.DecimalField(max_digits=12, decimal_places=2)

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def save(self, *args, **kwargs):
    self.updated_at = timezone.now()
    super().save(*args, **kwargs)
