# ticks/models.py
from django.db import models

class LearnerStatus(models.Model):
    learner_id = models.CharField(max_length=36, unique=True)  # Unique identifier from localStorage
    first_name = models.CharField(max_length=20)  # Mandatory learner name
    room_code = models.CharField(max_length=10)  # Room identifier (e.g., "M2")
    status = models.CharField(max_length=5, blank=True)  # Status (e.g., "tick", "cross"")
    answer = models.CharField(max_length=20, blank=True, null=True)  # Optional short answer
    timestamp = models.DateTimeField(auto_now=True)  # Auto-updated when learner sends data

    def __str__(self):
        return f"{self.room_code} - {self.first_name}: {self.status}"
