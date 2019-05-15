from django.shortcuts import render
from rest_framework import viewsets

from wcg.models import Request
from wcg.serializers import RequestSerializer


class RequestView(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer

    def perform_create(self, serializer):
        serializer.save()
