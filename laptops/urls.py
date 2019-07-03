from django.urls import path

from laptops import views

from .views import (
    product_create_view, 
    product_detail_view, 
    product_delete_view,
    product_list_view,
    product_update_view,
    home,
    about,
    contact,
    login,
    register,
    logout,
    category_list_view,
    category_detail_view,
)

app_name = 'laptops'
urlpatterns = [
    path('home',home,name='home-page'),
    path('about',about,name='about-page'),
    path('contact',contact,name='contact-page'),
    path('login',login,name='login-page'),
    path('register',register,name='register-page'),
    path('logout',logout,name='logout-page'),
    path('list', product_list_view, name='product-list'),
    path('', category_list_view, name='category-list'),
    path('category/<int:id>/', category_detail_view, name='category-detail'),
    path('create/', product_create_view, name='product-list'),
    path('<int:id>/', product_detail_view, name='product-detail'),
    path('<int:id>/update/', product_update_view, name='product-update'),
    path('<int:id>/delete/', product_delete_view, name='product-delete'),
]