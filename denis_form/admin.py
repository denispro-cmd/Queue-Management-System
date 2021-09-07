from django.contrib import admin
from .models import Token


class TokenAdmin(admin.ModelAdmin):
    list_display = ['firstname','lastname','token']


admin.site.register(Token)