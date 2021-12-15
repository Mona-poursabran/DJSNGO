from django.db import models

# Create your models here.

class StatusManager(models.Manager):
    def available(self):
        return self.get_queryset().filter(status= True)

    def unavailable(self):
        return self.get_queryset().filter(status= False)

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    brand_name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    created_date = models.DateField()
    status = models.BooleanField(default=False)
    objects = models.Manager()
    """
        new manager for status:
    """
    status_result = StatusManager()

    def __str__(self) -> str:
        return self.product_name

