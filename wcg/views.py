from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from wcg.models import Request, WordCloud
from wcg.serializers import RequestSerializer, WordCloudSerializer


class RequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all().order_by('requested_at')
    serializer_class = RequestSerializer

    @detail_route(methods=['post'])
    def generate_wordCloud(self, req, pk=None):

    def perform_create(self, serializer):
        serializer.save()


class WordCloudViewSet(viewsets.ModelViewSet):
    queryset = WordCloud.objects.all().order_by('requested_at')
    serializer_class = WordCloudSerializer

    def perform_create(self, serializer):
        serializer.save()


def generate_wordCloud(req):
    if req.method == "POST":
        new_wordCloud = WordCloud.objects.create(
            request=req.POST['request'],
            wordCloud=req.POST['wordCloud'],
        )
        # TODO: 어떻게 구현하지

    else:
        content = {'please move along': 'nothing to see here'}
        raise Response(content, status=status.HTTP_400_BAD_REQUEST)
