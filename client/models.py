import os

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.models import AbstractUser
from django.db import models
from gag.helpers import UploadTo


class User(AbstractUser):
    photo = models.ImageField(upload_to=UploadTo("Profile"))

    class Meta:
        verbose_name = "Foydalanuvchi"
        verbose_name_plural = "Foydalanuvchilar"

    @property
    def avatar(self):
        if self.photo:
            return self.photo.url

        return os.path.join(settings.STATIC_URL, "img/no_avatar.jpg")
