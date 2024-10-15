from django.db import models
from brand.models import Brands


#type class
class Type(models.Model):
    typeName = models.CharField(max_length=30)
    slug = models.CharField(max_length=30, default=None, null=True, blank=True)

    def __str__(self):
        return self.typeName

#category class
class Category(models.Model):
    categoryName = models.CharField(max_length=100)
    slug = models.CharField(max_length=30, default=None, null=True, blank=True)
    typeTitle = models.ForeignKey(Type, on_delete=models.CASCADE, null=True,blank=True)

    def __str__(self):
        return self.categoryName

# Create your models here.
class Products(models.Model):
    productName = models.CharField(max_length=150)
    barndName = models.ForeignKey(Brands, on_delete=models.CASCADE, null=True,blank=True)
    categoryTitle = models.ForeignKey(Category, on_delete=models.CASCADE, null=True,blank=True)
    info1 = models.CharField(max_length=200, blank=True)
    info2 = models.CharField(max_length=200, blank=True)
    info3 = models.CharField(max_length=200, blank=True)
    info4 = models.CharField(max_length=200, blank=True)
    info5 = models.CharField(max_length=200, blank=True)
    info6 = models.CharField(max_length=200, blank=True)
    info7 = models.CharField(max_length=200, blank=True)
    info8 = models.CharField(max_length=200, blank=True)
    info9 = models.CharField(max_length=200, blank=True)
    info10 = models.CharField(max_length=200, blank=True)
    info11 = models.CharField(max_length=200, blank=True)
    info12 = models.CharField(max_length=200, blank=True)
    info13 = models.CharField(max_length=200, blank=True)
    info14 = models.CharField(max_length=200, blank=True)
    info15 = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    productImage = models.ImageField(default='fallback.jpg')

    def __str__(self):
        return self.productName