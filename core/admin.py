from django.contrib import admin
from django import forms
from core.models import GuestbookEntry

class GuestbookEntryAdmin(admin.ModelAdmin):
    ordering = ('created_date',)
    list_display = ('name', 'display',)
    list_editable = ('display',)
    fieldsets = [
        ('Information', { 'fields' : ['name', 'message', 'display']})
    ]

admin.site.register(GuestbookEntry,GuestbookEntryAdmin)