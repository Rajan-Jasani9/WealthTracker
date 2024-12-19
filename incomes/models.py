from django.db import models
from debt.models import CommonInfo
# enums   

class Salary(CommonInfo):
    
    name = models.CharField(max_length=255)
    description = models.TextField()
    amount = models.FloatField()



class Income(CommonInfo):
    
    # Source of the income (e.g., Salary, Freelance, Investment)
    description = models.TextField(blank=True, null=True)
    source = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_received = models.DateField()
    is_salary = models.BooleanField(default=False)
    salary = models.ForeignKey(Salary, models.CASCADE, null=True)
    # Optional category field (e.g., "Passive", "Active", "One-time")
    category = models.CharField(max_length=100, blank=True, null=True)

    # Timestamp when the entry was created
    created_at = models.DateTimeField(auto_now_add=True)

    # Timestamp when the entry was last updated
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.source} - {self.amount}"
