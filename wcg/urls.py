from django.urls import path

from . import views

app_name = 'wcg'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('order/<int:pk>/', views.DetailView.as_view(), name='order_detail'),
    path('order/', views.get_orders, name='order_list')

]
