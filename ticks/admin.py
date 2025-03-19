from django.contrib import admin

# Register your models here.
from .models import UserChoice

@admin.register(UserChoice)
class UserChoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'choice', 'timestamp')  # Show these columns
    list_filter = ('choice', 'timestamp')  # Add filters
    search_fields = ('choice',)  # Allow searching
    ordering = ('-timestamp',)  # Order by latest first
