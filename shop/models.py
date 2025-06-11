from django.db import models
import datetime
from persiantools.jdatetime import JalaliDate
from django.core.validators import FileExtensionValidator


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Customer(models.Model):
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=40)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Product(models.Model):
    # states = ((1"Basic"),(2""),(3""))
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=12, default=0, decimal_places=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to="upload/product/")
    # video = models.FileField(
    #     upload_to="upload/video/",
    #     null=True,
    #     validators=[FileExtensionValidator(allowed_extensions=["mp4", "mkv"])],
    # )

    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0, decimal_places=0, max_digits=12)
    # percent_show = models.IntegerField()

    def __str__(self):
        return self.name


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    address = models.TextField()
    phone = models.CharField(max_length=20, blank=True)
    date = models.DateField(default=(datetime.datetime.now))

    def __str__(self):
        return self.product
