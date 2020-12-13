from django.db import models

class PaymentDetails(models.Model):
  CreditCardNumber = models.CharField(unique=True, blank=False, max_length = 19)
  CardHolder = models.CharField(blank=False, max_length= 40)
  ExpirationDate = models.DateField(blank=False)
  SecurityCode = models.IntegerField(max_length=3)
  Amount = models.DecimalField(max_digits=12, decimal_places=2)