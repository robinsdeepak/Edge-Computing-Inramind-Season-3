from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


# Create your models here.
class Invoice(models.Model):
    class Meta:
        verbose_name = "Invoice"
        db_table = "Invoice"

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    invoice_timestamp = models.DateTimeField(default=timezone.now)


class Product(models.Model):
    class Meta:
        verbose_name = "product"
        db_table = "product"

    product_name = models.CharField(max_length=200)
    # category = models.CharField(max_length=10,
    #                             choices=("Small", "Medium", "Large")
    #                             )
    price = models.DecimalField(max_digits=9, decimal_places=2)


# class product_category(models.Model):

class InvoiceProducts(models.Model):
    class Meta:
        verbose_name = "Invoice Products"
        db_table = "invoice_products"

    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
