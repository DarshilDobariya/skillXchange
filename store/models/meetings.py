from django.db import models
from .customer import Customer
from django.utils import timezone

class Meeting(models.Model):
    title = models.CharField(max_length=255)  # Meeting title
    scheduled_by = models.ForeignKey(
        'Customer', on_delete=models.CASCADE, related_name='scheduled_meetings'
    )  # Customer who scheduled the meeting
    participants = models.ManyToManyField(
        'Customer', related_name='invited_meetings'
    )  # Customers invited to the meeting
    participant_emails = models.JSONField()  # Array of participant emails
    meeting_link = models.URLField()  # Unique meeting link
    meeting_code = models.CharField(max_length=10, unique=True)  # Random meeting code

    def __str__(self):
        return self.title
