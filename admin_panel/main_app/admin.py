from django.contrib import admin
from .models.user_model import UserModel

@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')
