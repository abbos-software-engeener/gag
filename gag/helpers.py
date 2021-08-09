import os
from datetime import datetime
from django.utils.deconstruct import deconstructible


@deconstructible()
class UploadTo:
    def __init__(self, folder):
        self.folder = folder

    def __call__(self, instance, filename):
        ext = os.path.splitext(filename)[1]

        return "{}/{:%Y-%m}/{:%Y-%m-%d-%H-%M-%S}".format(
            self.folder,
            datetime.now(),
            datetime.now(),
            ext

        )


