from django.urls import path
from . import views

urlpatterns = [
    path('home',views.home),
    path('login',views.login),
    path('myorders',views.myorders),
    path('mycart',views.mycart),
]