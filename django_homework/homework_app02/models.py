from django.db import models

# Create your models here.


class Client(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    number = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    date_register = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} {self.number}'


class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    price = models.FloatField()
    count = models.IntegerField()
    date_published = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}   {self.description}'


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField()
    date_buy = models.DateField(auto_now_add=True)
