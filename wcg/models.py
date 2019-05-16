from datetime import datetime

from pytz import timezone

from colorfield.fields import ColorField
from django.db import models
from django.conf import settings


def default_mask_image_path():
    name = "default_mask_image.jpeg"

    return media_path('mask_image', name)


def media_path(type, name):
    """

    :param type:
    :param name:
    :return:
    """
    return "{type}/{name}".format(
        type=type,
        name=name
    )


class Font(models.Model):
    def __str__(self):
        return self.name

    def font_path(self, filename):
        """
        Font file path setting
        :param filename: original name of the font to upload
        :return: path to upload to
        """
        name = self.name + "." + filename.split('.')[-1]
        return media_path('font', name)

    name = models.CharField(max_length=100)
    font_file = models.FileField(upload_to=font_path)


class Order(models.Model):
    def __str__(self):
        return "{client}-{title}-{date}_{time}".format(
            client=self.client,
            title=self.title,
            date=datetime.strftime(self.ordered_at_korean_time, "%y%m%d"),
            time=datetime.strftime(self.ordered_at_korean_time, "%H%M%S")
        )

    @property
    def ordered_at_korean_time(self):
        korean_timezone = timezone(settings.TIME_ZONE)
        return self.ordered_at.astimezone(korean_timezone)

    def mask_image_path(self, filename):
        """

        :param self: instance.
        :param filename: mask image's file name
        :return: mask image's path to save in server.
        """

        date = datetime.strftime(self.ordered_at_korean_time, "%y%m%d")
        time = datetime.strftime(self.ordered_at_korean_time, "%H%M%S")
        extension = filename.split('.')[-1]

        name = "{date}/{title}_{date}_{time}.{extension}".format(
            date=date,
            title=self.title,
            time=time,
            extension=extension
        )
        return media_path("mask_image", name)

    client = models.CharField(max_length=200, default="unknown")
    title = models.CharField(max_length=100)
    data = models.TextField(default="")
    font = models.ForeignKey(Font, models.SET_DEFAULT, default=None)
    mask_image = models.ImageField(upload_to=mask_image_path, blank=True)
    background_color = ColorField(default="#FFFFFF")
    ordered_at = models.DateTimeField(auto_now_add=True)


class WordCloud(models.Model):
    def __str__(self):
        return self.order.title + "_" + str(datetime.strftime(self.order.oredered_at_korean_time, "%y%m%d_%H%M%S"))

    def word_cloud_path(self, filename):
        date = datetime.strftime(self.order.oredered_at_korean_time, "%y%m%d")
        time = datetime.strftime(self.order.ordered_at_korean_time, "%H%M%S")
        extension = filename.split('.')[-1]

        name = "{date}/{title}_{date}_{time}.{extension}".format(
            date=date,
            title=self.order.title,
            time=time,
            extension=extension
        )

        return media_path("mask_image", name)

    order = models.ForeignKey(Order, models.CASCADE)
    wordCloud = models.FileField(upload_to=word_cloud_path, blank=True)
