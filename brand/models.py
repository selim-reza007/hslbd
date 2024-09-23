from django.db import models

# Create your models here.
class Brands(models.Model):
    brandName = models.CharField(max_length=50)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.brandName
    