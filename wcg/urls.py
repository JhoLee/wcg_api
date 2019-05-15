from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import RequestView

request_list = RequestView.as_view({
    'post': 'create',
    'get': 'list',
})

request_detail = RequestView.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = format_suffix_patterns([
    path('requests/', request_list, name='request_list'),
    path('requests/<int:pk>/', request_detail, name='request_detail'),

])
