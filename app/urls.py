from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('watch/', views.product, name = 'product'),
    path('home/', views.landing, name = 'landing'),
]