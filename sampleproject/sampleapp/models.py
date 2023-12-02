from django.db import models

# class LoginModel (models.Model):
#     username = models.CharField(max_length=256)
#     password = models.TextField()
#     img = models.ImageField(upload_to='images/')
#     def __str__(self) -> str:
#         return self.name


# class RegisterModel (models.Model):
#     username = models.CharField(max_length=256)
#     password = models.TimeField()
#     img = models.ImageField(upload_to='images/')
#     def __str__(self) -> str:
#         return self.name
    
    
# class ForgottModel(models.Model):
#     Email = models.EmailField(max_length=254)
#     PhoneNo =models.IntegerField()
# def __str__(self) -> str:
#     return self.name  


class ForgottModel(models.Model):
    Title = models.CharField(max_length=50)
    Year =models.TextField()
    Summary = models.CharField(max_length=256)
def __str__(self) -> str:
    return self.name 
    
    

    
    
    
    
    

