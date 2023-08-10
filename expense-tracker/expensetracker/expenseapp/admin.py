from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from . import models


# Register your models here.

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    pass


admin.site.register(models.Category)

admin.site.register(models.Expense)

admin.site.register(models.Income)
