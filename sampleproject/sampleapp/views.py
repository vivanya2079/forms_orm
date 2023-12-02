from django.shortcuts import render
# from django.http import HttpResponse
# from django.template import loader
from .models import ForgottModel
from .forms import ForgottForm

# def members(request):
#     movie_data = {
#         'movies': [
#             {
#                 'title': 'Godfather',
#                 'year': 2005,
#                 'success': False
#             },
#             {
#                 'title': 'Titanic',
#                 'year': 2012,
#                 'summary': 'story of underworld',
#                 'success': False
#             },
#             {
#                 'title': 'love in the air',
#                 'year': 2020,
#                 'summary': 'story of underworld',
#                 'success': False
#             },
#             {
#                 'title': 'together',
#                 'year': 2021,
#                 'summary': 'story of underworld',
#                 'success': False
#             },
#             {
#                 'title': 'ailongnhai',
#                 'year': 2022,
#                 'summary': 'story of underworld',
#                 'success': False
#             }
#         ]
#     }

#     template = loader.get_template('dictionary.html')
#     return HttpResponse(template.render(movie_data, request))

# Create your views here.

# def home_view(request):
#     context ={}
#     form = ForgottForm(request.POST or None, request.FILES or None)
#     if form.is_valid():
#         form.save()
#     context['form']= form
#     return render(request, "home_view.html", context)


def hey(request):
    context ={}
    form = ForgottForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
    context['form']= form
    return render(request, "hey.html", context)
        
