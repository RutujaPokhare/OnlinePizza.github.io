from django.db import models

# Create your models here.
class Category(models.Model):
    Category_name = models.CharField(max_length=20)

    def __str__(self):
        return self.Category_name

    class Meta:
        db_table = "Category"

size_choices = (
    ("R","regular"),
    ("M","Medium"),
    ("L","Large"),
)

class Product(models.Model):
    pname = models.CharField(max_length=20)
    price = models.FloatField(default=200)
    description = models.CharField(max_length=50)
    size = models.CharField(max_length=20,choices = size_choices)
    quantity = models.IntegerField()
    image = models.ImageField(default='abc.jpg',upload_to = 'Images')
    cat = models.ForeignKey(to='Category',on_delete=models.CASCADE)


    class Meta:
        db_table = "Product"

class UserInfo(models.Model):
    username = models.CharField(max_length = 20,primary_key=True)
    password = models.CharField(max_length = 20)
    email = models.EmailField(max_length = 100)

    class meta:
        db_table = 'UserInfo'

class PaymentMaster(models.Model):
    cardno = models.CharField(max_length=20)
    cvv = models.CharField(max_length=4)
    expiry = models.CharField(max_length=20)
    balance = models.FloatField(default=10000)

    class meta:
        db_table = "PaymentMaster"



        
