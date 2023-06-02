
from django.db import models
from AdminApp.models import UserInfo,Product
from datetime import datetime

# Create your models here.

class MyCart(models.Model):
    user = models.ForeignKey(to="AdminApp.UserInfo",
            on_delete=models.CASCADE)

    pizza = models.ForeignKey(to="AdminApp.Product",
            on_delete=models.CASCADE)

    quantity= models.IntegerField()

    class Meta:
        db_table = "MyCart"

class OrderMaster(models.Model):
        user = models.ForeignKey(to="AdminApp.UserInfo",on_delete=models.CASCADE)
        amount = models.FloatField(default=1000)
        dateOfOrder = models.DateTimeField(default=datetime.now)
        details = models.CharField(max_length=200)

        class meta:
                db_table = "OrderMaster"

