from django.shortcuts import render
from django.views.generic.edit import CreateView,UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import DeleteView
from django.urls import reverse_lazy

from .models import LoginModel
# Create your views here.
class LoginCreate(CreateView):
    model= LoginModel
    fields= ('username','password')
    template_name='loginmodel_form.html'
    success_url= '/success/'
    
class LoginList(ListView):
    model= LoginModel
    template_name='login_list.html'
    context_object_name='login_list'
    
class LoginDetailView(DetailView):
    model= LoginModel
    template_name= 'loginmodel_detail.html'
    context_object_name= 'login_model' 
    
class LoginUpdateView(UpdateView):
    model= LoginModel
    fields= ["username","password"]
    template_name= 'loginmodel_update.html'
    success_url= '/UpdateView/'   
    
class LoginDeleteView(DeleteView):
    model= LoginModel
    template_name='login_confirm_delete.html'
    success_url= reverse_lazy('LoginList')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["username"] = 'Confirm Delete Login Object'
        return context
        
 