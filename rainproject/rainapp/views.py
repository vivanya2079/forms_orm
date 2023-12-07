from django.shortcuts import render
from django.views.generic.edit import CreateView,UpdateView
from django.views.generic.list import ListView
from .models import ForgottModel
from django.views.generic.detail import DetailView
from django.views.generic import DeleteView
from django.urls import reverse_lazy


class ForgottCreate(CreateView):
    model= ForgottModel
    fields= ('email','phone')
    template_name='forgottmodel_form.html'
    success_url= '/success/'
    
class ForgottList(ListView):
    model= ForgottModel
    template_name='forgott_list.html'
    context_object_name='forgott_list'
    
class ForgottDetailView(DetailView):
    model= ForgottModel
    template_name= 'forgottmodel_detail.html'
    context_object_name= 'Forgott_model'
    
class ForgottUpdateView(UpdateView):
    model= ForgottModel
    fields= ["email","phone"]
    template_name= 'forgottmodel_update.html'
    success_url= '/UpdateView/'    
    
class ForgottDeleteView(DeleteView):
    model= ForgottModel
    template_name='forgott_confirm_delete.html'
    success_url= reverse_lazy('ForgottList')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["email"] = 'Confirm Delete Forgott Object'
        return context     