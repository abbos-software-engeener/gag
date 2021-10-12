from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    class Meta:
        model = User
        fields = '__all__'


admin.site.register()