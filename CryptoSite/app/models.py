from django.db import models

# Create your models here.

class TradingPairs(models.Model):
    sell = models.CharField(max_length=100)
    buy = models.CharField(max_length=100)
