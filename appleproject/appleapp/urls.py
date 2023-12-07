from django.urls import path
from .views import RegisterCreate,RegisterList,RegisterDetailView,RegisterUpdateView,RegisterDeleteView

urlpatterns = [
    path('register/create',RegisterCreate.as_view(),name='RegisterCreate'),
    path('register/list',RegisterList.as_view(),name='RegisterList'),
    path('register/detail/<int:pk>/',RegisterDetailView.as_view(),name='RegisterDetailView'),
    path('register/update/<int:pk>/',RegisterUpdateView.as_view(),name='RegisterUpdateView'),
    path('register/delete/<int:pk>/',RegisterDeleteView.as_view(),name='RegisterDeleteView'),

]