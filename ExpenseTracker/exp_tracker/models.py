from django.db import models
from datetime import datetime

# Create your models here.
class Account(models.Model):
    name = models.CharField(max_length=100)
    expense = models.FloatField(default=0.0)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    expense_list = models.ManyToManyField('Expense', blank=True)

class Expense(models.Model):
    name = models.CharField(max_length=100)
    amount = models.FloatField()
    date = models.DateTimeField(default=datetime.now, blank=True)
    long_term = models.BooleanField(default=False)
    interest_rate = models.FloatField(default=0.0)
    end_date = models.DateTimeField(null=True, blank=True)
    monthly_expense = models.FloatField(default=0.0, null=True, blank=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self.long_term :
            self.monthly_expense = calculate_monthly_expense
        super(Expenses, self).save(*args, **kwargs)

    def calculate_monthly_expense(self):
        if self.long_term:
            if self.interest_rate == 0:
                return self.amount / ((self.end_date - self.date) / 30)
            else:
                months = (self.end_date.year - datetime.now().year) * 12 + (self.end_date.month - datetime.now().month)
                montlhy_rate = self.interest_rate / 12 / 100
                montlhy_expense = (self.amount * montlhy_rate) / (1 - (1 + montlhy_rate) ** -months)
        else:
                return self.montlhy_expense