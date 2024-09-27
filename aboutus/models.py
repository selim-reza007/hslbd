from django.db import models

# Create your models here.
class CompanyInfo(models.Model):
    mobile = models.CharField(max_length=30)
    email = models.EmailField(max_length=150)
    profile = models.FileField(upload_to='pdfs/')

    def __str__(self):
        return self.email