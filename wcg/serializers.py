from rest_framework import serializers
from .models import Request, WordCloud


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ('requester', 'title', 'data', 'font', 'mask_image', 'background_color',)


class WordCloudSerializer(serializers.ModelSerializer):
    request = RequestSerializer(read_only=True)

    class Meta:
        model = WordCloud
        fields = ('wordCloud',)
