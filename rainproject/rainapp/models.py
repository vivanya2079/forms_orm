from django.db import models

class ForgottModel(models.Model):
    email =models.EmailField(max_length=254)
    phone =models.IntegerField()
    def __str__(self):
        return self.email

# Create your models here.
