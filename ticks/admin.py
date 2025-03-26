from django.contrib import admin
from .models import LearnerStatus

@admin.register(LearnerStatus)
class LearnerStatusAdmin(admin.ModelAdmin):
    list_display = ('room_code', 'first_name', 'status', 'answer', 'timestamp')
    search_fields = ('room_code', 'first_name', 'status')
    list_filter = ('room_code', 'status')
    ordering = ('-timestamp',)
