from django.db import models

# Create your models here.


class Client(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    date_register = models.DateField(auto_now_add=True)
    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    price = models.FloatField()
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='images/')
    date_published = models.DateField(auto_now_add=True)


    def __str__(self):
        return f'{self.name}'


class Order(models.Model):
    client = models.ForeignKey(
        Client, on_delete=models.CASCADE, related_name='orders')
    product = models.ManyToManyField(Product, related_name='in_order')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
