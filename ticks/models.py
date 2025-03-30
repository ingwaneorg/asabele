# ticks/models.py
from django.db import models

class LearnerStatus(models.Model):
    learner_id = models.CharField(max_length=50)
    first_name = models.CharField(max_length=20)
    room_code = models.CharField(max_length=10)
    status = models.CharField(max_length=5, blank=True)
    answer = models.CharField(max_length=20, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.room_code} - {self.first_name}: {self.status}"
