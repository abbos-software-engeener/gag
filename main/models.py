import os

from django.db import models
from gag.helpers import UploadTo
from gag.mixins import TranslateMixin


class Category(TranslateMixin, models.Model):
    translate_fields = ['name']
    name_uz = models.CharField(max_length=50)
    name_ru = models.CharField(max_length=50)
    image = models.ImageField(upload_to=UploadTo("category"))

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"

    def __str__(self):
        return self.name_uz


class Post(models.Model):
    category = models.ForeignKey('main.Category', on_delete=models.RESTRICT)
    user = models.ForeignKey("client.User", on_delete=models.RESTRICT)
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    fields = models.FileField(blank=True, null=True)
    comment = models.TextField(verbose_name="Izoh")

    @property
    def ext(self):
        return (os.path.splitext(self.fields.name)[1])[1:].lower()

    @property
    def is_image(self):
        return self.ext in ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'webp']

    @property
    def is_video(self):
        return self.ext in ['mp4', 'mpeg']

    @property
    def is_audio(self):
        return self.ext in ['mp3', 'wav']


class Post_Comment(models.Model):
    parent = models.ForeignKey('main.Post_Comment', null=True, default=None, on_delete=models.RESTRICT)
    post = models.ForeignKey('main.Post', null=True, default=None, on_delete=models.RESTRICT)
    user = models.ForeignKey('client.User', default=None, on_delete=models.RESTRICT)
    comment = models.TextField(verbose_name="izoh")
    image = models.ImageField(upload_to=UploadTo("comment"), null=True, default=None, blank=True)
    like = models.CharField(max_length=100, default=0)
    dislike = models.CharField(max_length=100, default=0)
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
















































