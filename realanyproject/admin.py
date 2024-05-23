from django.contrib import admin
from .models import Movie, Music, Book, User

admin.site.register(Movie)
admin.site.register(Music)
admin.site.register(Book)

from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    model = User
    fieldsets = (
        (None, {'fields': ('username', 'phone_number','user_gender',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('phone_number','user_gender',)}),
    )
    list_display = ['username', 'phone_number','user_gender', 'is_active',]

admin.site.register(User, CustomUserAdmin)
