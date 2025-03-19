from django.db import models

# Create your models here.

class UserChoice(models.Model):
    choice = models.CharField(max_length=1, choices=[('A', 'Option A'), ('B', 'Option B')])
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.choice
