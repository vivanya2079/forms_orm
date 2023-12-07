from django.db import models
class LoginModel(models.Model):
    username=models.CharField(max_length=256)
    password=models.TextField()
    def __str__(self):
        return self.username

# Create your models here.
