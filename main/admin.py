from django.contrib import admin
from django.contrib.admin import ModelAdmin
from main.models import Category


class MainAdmin(admin.ModelAdmin):
    class Meta:
        model = Category


admin.site.register(Category, MainAdmin)
