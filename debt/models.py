from django.db import models


class DebtType(models.TextChoices):
  PERSONAL_LOAN = "PERSONAL_LOAN", "Personal Loan"
  MORTGAGE = "MORTGAGE", "Mortgage"
  STUDENT_LOAN = "STUDENT_LOAN", "Student Loan"
  CREDIT_CARD = "CREDIT_CARD", "Credit Card"
  BUSINESS_LOAN = "BUSINESS_LOAN", "Business Loan"
  AUTO_LOAN = "AUTO_LOAN", "Auto Loan"
  FRIENDS_FAMILY = "FRIENDS_FAMILY", "Borrowed from Friends/Family"
  OTHER = "OTHER", "Other"


class DebtStatus(models.TextChoices):
  ACTIVE = "ACTIVE", "Active"
  PAID_OFF = "PAID_OFF", "Paid Off"
  DEFAULTED = "DEFAULTED", "Defaulted"


# Create your models here.


class Lender(models.Model):

  name = models.CharField(max_length=255)
  is_institution = models.BooleanField(default=False)
  contact_number = models.CharField(max_length=255, blank=True)
  email = models.EmailField(blank=True)


class Debt(models.Model):
  name = models.CharField(max_length=255)
  debt_type = models.CharField(
      max_length=50,
      choices=DebtType.choices,
      default=DebtType.OTHER,
  )
  principal_amount = models.DecimalField(
      max_digits=12,
      decimal_places=2,
      help_text="Original amount of the debt",
  )
  outstanding_amount = models.DecimalField(
      max_digits=12,
      decimal_places=2,
      help_text="Current unpaid amount of the debt",
  )
  interest_rate = models.DecimalField(
      max_digits=5,
      decimal_places=2,
      help_text="Interest rate as a percentage (e.g., 5.5 for 5.5%)",
  )
  start_date = models.DateField(help_text="Start date of the debt")
  has_emis = models.BooleanField(default=False)
  emi_amount = models.DecimalField(
      max_digits=10,
      decimal_places=2,
  )
  total_installments = models.IntegerField(
      help_text="Total number of installments", )
  installments_paid = models.IntegerField(
      help_text="number of installments paid", )
  due_date = models.DateField(
      help_text="Due date or maturity date of the debt", null=True, blank=True)
  status = models.CharField(
      max_length=20,
      choices=DebtStatus.choices,
      default=DebtStatus.ACTIVE,
  )
  currency = models.CharField(max_length=10,
                              default="USD",
                              help_text="Currency of the debt")
  notes = models.TextField(blank=True,
                           help_text="Optional notes about the debt")
  lender = models.ForeignKey(Lender,
                             on_delete=models.CASCADE,
                             null=True,
                             blank=True)

  def __str__(self):
    return f"{self.name} ({self.debt_type})"
