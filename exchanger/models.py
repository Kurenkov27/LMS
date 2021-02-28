from django.db import models

# Create your models here.
from django.utils import timezone


def get_color_status(a):
    if a == 1:
        return "green"
    elif a == -1:
        return "red"
    else:
        return "yellow"


class ExchangeRate(models.Model):
    id = models.CharField(max_length=6, primary_key=True)
    currency_a = models.CharField(max_length=3)
    currency_b = models.CharField(max_length=3)
    buy = models.DecimalField(max_digits=8, decimal_places=2)
    buy_status = models.DecimalField(max_digits=1, decimal_places=0, default=0)
    sell = models.DecimalField(max_digits=8, decimal_places=2)
    sell_status = models.DecimalField(max_digits=1, decimal_places=0, default=0)
    created_time = models.DateTimeField(default=timezone.now)

    def to_dict(self):
        currency_a = self.currency_a.lower()
        return {
            f"{currency_a}_buy": self.buy,
            f"{currency_a}_sell": self.sell,
            f"{currency_a}_buy_status": get_color_status(self.buy_status),
            f"{currency_a}_sell_status": get_color_status(self.sell_status)
        }
