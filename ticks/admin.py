from django.contrib import admin
from .models import LearnerStatus

@admin.register(LearnerStatus)
class LearnerStatusAdmin(admin.ModelAdmin):
    list_display = ('learner_id','room_code','first_name','status','timestamp')
    search_fields = ('room_code','first_name','status')
    list_filter = ('room_code','status')
    ordering = ('-timestamp',)
