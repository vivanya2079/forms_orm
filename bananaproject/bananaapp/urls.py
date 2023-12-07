from django.urls import path
from .views import LoginCreate,LoginList,LoginDetailView,LoginUpdateView,LoginDeleteView

urlpatterns = [
    path('login/create',LoginCreate.as_view(),name='LoginCreate'),
    path('login/list',LoginList.as_view(),name='LoginList'),
    path('login/detail/<int:pk>/',LoginDetailView.as_view(),name='LoginDetailView'),
    path('login/update/<int:pk>/',LoginUpdateView.as_view(),name='LoginUpdateView'),
    path('login/delete/<int:pk>/',LoginDeleteView.as_view(),name='LoginDeleteView'),
    
    
]
