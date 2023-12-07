from django.shortcuts import render
from django.views.generic.edit import CreateView,UpdateView
from django.views.generic.list import ListView
from .models import RegisterModel
from django.views.generic.detail import DetailView
from django.views.generic import DeleteView
from django.urls import reverse_lazy



class RegisterCreate(CreateView):
    model= RegisterModel
    fields= ('username','email','password')
    template_name='registermodel_form.html'
    success_url= '/success/'
    
class RegisterList(ListView):
    model= RegisterModel
    template_name='register_list.html'
    context_object_name='register_list'
    
class RegisterDetailView(DetailView):
    model= RegisterModel
    template_name= 'registermodel_detail.html'
    context_object_name= 'Register_model'     
    
class RegisterUpdateView(UpdateView):
    model= RegisterModel
    fields= ["username","email","password"]
    template_name= 'registermodel_update.html'
    success_url= '/UpdateView/' 
    
class RegisterDeleteView(DeleteView):
    model= RegisterModel
    template_name='register_confirm_delete.html'
    success_url= reverse_lazy('RegisterList')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["username"] = 'Confirm Delete Login Object'
        return context