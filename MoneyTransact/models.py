from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Balance(models.Model):
    RUPEES = 'Rs'
    DOLLAR = '$'
    OTHERS = 'o/w'
    Currency_CHOICES = (
        (RUPEES, 'Rupees'),
        (DOLLAR, 'Dollar'),
        (OTHERS, 'Others'),
    )
    currency =models.CharField(max_length=3,
        choices=Currency_CHOICES,
        default=RUPEES,
    )
    Giver = models.CharField(max_length=50)
    taker = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    reason = models.CharField(max_length=250)
    place = models.CharField(max_length=50)


    def __str__(self):
        return "giver : " + self.Giver + " taker : " + self.taker + " amount:  " + str(self.amount)

