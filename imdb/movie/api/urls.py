from django.urls import path
from . views import (Streamlist, Streamdetails, Movielist, Moviedetails)

urlpatterns = [
    path('', Streamlist.as_view(), name='streamlist'),
    path('<int:pk>/', Streamdetails.as_view(), name='streamdetails'),
    path('movielist/', Movielist.as_view(), name='movielist'),
    path('movielist/<int:pk>/', Moviedetails.as_view(), name='moviedetails'),
    
]
