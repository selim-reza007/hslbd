from django.db import models

# Create your models here.
class Message(models.Model):
    firstName = models.CharField(max_length=15, blank=True)
    lastName = models.CharField(max_length=15, blank=True)
    companyName = models.CharField(max_length=50, blank=True)
    mobile = models.CharField(max_length=20)
    email = models.EmailField(max_length=200)
    messageText = models.TextField()
    status = models.BooleanField(default=False, blank=True)
    messageRead = models.BooleanField(default=False, blank=True)
    receivedDate = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.email