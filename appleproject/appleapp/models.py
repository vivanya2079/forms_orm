from django.db import models

class RegisterModel(models.Model):
    username = models.CharField(max_length=250)
    email =models.EmailField(max_length=254)
    password =models.TextField()
    def __str__(self):
        return self.username
# Create your models here.
