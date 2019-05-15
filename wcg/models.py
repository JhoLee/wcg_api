import os
from datetime import datetime

from pytz import timezone
from time import strftime

from colorfield.fields import ColorField
from django.db import models
from django.conf import settings


def user_path(instance, filename):
    from random import choice
    import string

    arr = [choice(string.ascii_letters) for _ in range(8)]
    pid = ''.join(arr)
    extension = filename.split('.')[-1]

    return 'mask_image/%s.%s' % (pid, extension)


def mask_path(instance, filename):
    """

    :param instance: instance.
    :param filename: maks image's file name
    :return: mask image's path to save in server.
    """
    # TODO: Check file's extension.

    date = strftime("%y%m%d")
    time = strftime("%H%M%S")
    extension = filename.split('.')[-1]

    path = "mask_image/%s_%s_%s_%s.%s" % (instance.title, instance.font, date, time, extension)

    return path


def font_path():
    """

    :return:
    """
    return os.path.join(STATIC_ROOT, '/font')


class WordCloud(models.Model):
    def __str__(self):
        return self.title + "_" + datetime.strftime(self.uploaded_at, "%y%m%d_%H%M%S")

    @property
    def uploaded_at_korean_time(self):
        korean_timzeone = timezone(settings.TIME_ZONE)
        return self.uploaded_at.astimezone(korean_timzeone)

    title = models.CharField(max_length=100)
    mask_image = models.ImageField(upload_to=mask_path)
    font = models.CharField(max_length=50)
    data = models.TextField()
    background_color = ColorField(default="#FFFFFF")
    uploaded_at = models.DateTimeField(auto_now_add=True)


class MaskImage(models.Model):
    def __str__(self):
        return self.title + "_" + datetime.strftime(self.uploaded_at_korean_time, "%y%m%d_%H%M%S")

    @property
    def uploaded_at_korean_time(self):
        korean_timezone = timezone(settings.TIME_ZONE)
        return self.uploaded_at.astimezone(korean_timezone)

    def mask_path(self, filename):
        """

        :param self: instance.
        :param filename: maks image's file name
        :return: mask image's path to save in server.
        """
        # TODO: Check file's extension.

        date = strftime("%y%m%d")
        time = strftime("%H%M%S")
        extension = filename.split('.')[-1]

        path = "mask_image/%s_%s_%s.%s" % (self.title, date, time, extension)

        return path

    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to=mask_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)


class Font(models.Model):
    name = models.CharField(max_length=100)
    path = models.FilePathField(path=font_path)
