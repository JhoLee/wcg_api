from time import strftime

from django.db import models
from colorfield.fields import ColorField


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

    path = "%s_%s_%s_%s.%s" % (instance.title, instance.font, date, time, extension)

    return path


class WordCloud(models.Model):
    title = models.CharField(max_length=100)
    mask_image = models.ImageField(upload_to=mask_path)
    font = models.CharField(max_length=50)
    data = models.TextField()
    background_color = ColorField(default="#FFFFFF")
