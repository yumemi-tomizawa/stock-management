from django.db import models
from cash.models import Account

class Order(models.Model):
      user_account = models.ForeignKey(Account, on_delete=models.CASCADE, blank=True, null=True);
      ticker = models.CharField(max_length=10);
      acquisition_cost = models.FloatField();
      total_share = models.IntegerField();

      def __str__(self):
        return self.ticker

