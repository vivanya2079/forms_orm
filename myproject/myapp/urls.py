# from django.urls import path
# from .views import LoginCreate
# urlpatterns = [
#     path('',LoginCreate.as_view()),
# ]



from django.urls import path
 
# importing views from views..py
from .views import LoginList
urlpatterns = [
    path('', LoginList.as_view()),
]
