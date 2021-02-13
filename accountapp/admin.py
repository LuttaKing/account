from django.contrib import admin
from .models import Post,Account

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'date_joined', 'is_admin')