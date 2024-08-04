from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    """Mets Classe para Usuário"""

    model = CustomUser
    list_display = ["username", "is_staff", "is_active"]
    list_filter = ["is_staff", "is_active"]
    search_fields = ["username"]
    readonly_fields = ["date_joined", "last_login"]
    ordering = ["email"]