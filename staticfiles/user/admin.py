from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from user.forms import CustomUserChangeForm, CustomUserCreationForm
from user.models import User, DocFilesUser


class BaseUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ("email", "is_staff", "is_active",)
    list_filter = ("email", "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("user info", {"fields": ("is_active", "ent_result", "photo", "age", "gender")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2",
            )}
         ),
    )
    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(User, BaseUserAdmin)
admin.site.register(DocFilesUser)
