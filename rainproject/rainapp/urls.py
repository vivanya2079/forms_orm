from django.urls import path
from .views import ForgottCreate,ForgottList,ForgottDetailView,ForgottUpdateView,ForgottDeleteView

urlpatterns = [
    path('forgott/create',ForgottCreate.as_view(),name='ForgottCreate'),
    path('forgott/list',ForgottList.as_view(),name='ForgottList'),
    path('forgott/detail/<int:pk>/',ForgottDetailView.as_view(),name='ForgottDetailView'),
    path('forgott/update/<int:pk>/',ForgottUpdateView.as_view(),name='ForgottUpdateView'),
    path('forgott/delete/<int:pk>/',ForgottDeleteView.as_view(),name='ForgottDeleteView'),


    ]