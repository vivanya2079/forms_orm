# from django.urls import path
# from .views import RegisterCreate
# urlpatterns = [
#     path('',RegisterCreate.as_view()),
# ]


from django.urls import path
 
# importing views from views..py
from .views import RegisterList
urlpatterns = [
    path('', RegisterList.as_view()),
]
