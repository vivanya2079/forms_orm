# from django.shortcuts import render
# from django.views.generic.edit import CreateView
# from .models import LoginModel

# class LoginCreate(CreateView):
#     model=LoginModel
#     fields = ['username','password']
#     template_name ='loginmodel_form.html'
# Create your views here.


from django.views.generic.list import ListView
from .models import LoginModel
 
class LoginList(ListView):
 
    # specify the model for list view
    model = LoginModel
    
    template_name='login_list.html'
    context_object_name='login_list'
