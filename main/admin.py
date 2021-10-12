from django.contrib import admin
from django.contrib.admin import ModelAdmin
from main.models import *


class MainAdmin(admin.ModelAdmin):
    class Meta:
        model = Category


admin.site.register(Category, MainAdmin)

admin.site.register(Post_Comment)
admin.site.register(Post)
