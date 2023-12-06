# from django.shortcuts import render
# from django.views.generic.edit import CreateView
# from .models import RegisterModel

# class RegisterCreate(CreateView):
#     model=RegisterModel
#     fields = ['username','email','password']
#     template_name ='registermodel_form.html'
# Create your views here.


from django.views.generic.list import ListView
from .models import RegisterModel
 
class RegisterList(ListView):
 
    # specify the model for list view
    model = RegisterModel
    
    template_name='register_list.html'
    context_object_name='register_list'