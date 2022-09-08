from django.urls import path
from . import views

urlpatterns = [
path('shipping/', views.shipping, name='shipping'),
path('cart', views.cart, name='cart'),
path('payment', views.payment, name='payment'),
path('profile', views.profile, name='profile'),
path('favorites', views.favorites, name='favorites'),
path('edit/profile', views.edit_profile, name='edit_profile'),
]
