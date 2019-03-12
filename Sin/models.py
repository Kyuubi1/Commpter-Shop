from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Account(AbstractUser):
    sex_choice = ((0, 'Nữ'), (1, 'Nam'))
    address = models.CharField(default='', max_length=50)
    sex = models.IntegerField(choices=sex_choice, default='1')
    phone = models.IntegerField()

    def __str__(self):
        return self.username


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(default='', max_length=100)
    image = models.ImageField(blank=True, null=True)
    number = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    cost = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Service(models.Model):
    customer_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=13)

    def __str__(self):
        return self.customer_name


class FixService(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    fix = models.ForeignKey(Service, on_delete=models.CASCADE)
    employee = models.ForeignKey(Account, on_delete=models.CASCADE)
    error = models.CharField(max_length=100)
    is_guarantee = models.IntegerField()

    def __str__(self):
        return self.error


class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    number = models.IntegerField(default=0)

    def __str__(self):
        return self.product


class Payment(models.Model):
    customer = models.ForeignKey(Account, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    payment = models.IntegerField()

    def __str__(self):
        return self.customer


class Report(models.Model):
    fixed = models.ForeignKey(FixService, on_delete=models.CASCADE)
    assignee = models.ForeignKey(Account, on_delete=models.CASCADE)
    is_fixed = models.IntegerField(default=1)
    created_datetime = models.DateTimeField(auto_now_add=True)
    type_report = models.IntegerField(default=0)

    def __str__(self):
        if self.type_report == 1:
            return "Bảo hành "
        else:
            return "Giao hàng "
