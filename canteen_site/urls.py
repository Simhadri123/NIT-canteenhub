from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('ourvision/', views.ourvision, name='ourvision'),
    path('client-side/', views.clientside, name='clientside'),
    path('user-orders/', views.userorders, name='userorders'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('', views.signout, name='signout'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('get_cart_items/',views.get_cart_items,name='get_cart_items'),
    path('get_cart_status/',views.get_cart_status,name='get_cart_status'),
    path('clear_cart/',views.clear_cart,name='clear_cart'),
    path('place_order/',views.place_order,name='place_order'),
    path('increase_quantity/',views.increase_quantity,name='increase_quantity'),
    path('decrease_quantity/',views.decrease_quantity,name='decrease_quantity'),
    path('profile/', views.profile, name='profile'),

]