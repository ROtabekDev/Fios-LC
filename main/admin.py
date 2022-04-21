from django.contrib import admin
from .models import Contact, Appeal


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "text")


@admin.register(Appeal)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "text")
