from django.db import models

# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=20)
    expenditure_on_others = models.FloatField(default=0)
    expenditure_on_self = models.FloatField(default=0)
    amount_borrowed = models.FloatField(default=0)
    net_payment = models.FloatField(default=0)

    def __str__(self):
        return self.name



class Expenditure(models.Model):
    payer = models.ForeignKey(Member,on_delete=models.CASCADE)
    payee = models.CharField(max_length=20)
    amount = models.FloatField(default=0)
    description = models.CharField(max_length=20)
    
    def __str__(self):
        return self.description