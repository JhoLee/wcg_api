from django.urls import path

from . import views

app_name = 'wcg'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('order/', views.get_orders, name='order_list'),
    path('order/<int:pk>/', views.get_order_detail, name='order_detail'),

]
