from django.db import models
from django.conf import settings  # Import settings to access AUTH_USER_MODEL


class Conversation(models.Model):
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        participant_usernames = ', '.join([user.username for user in self.participants.all()[:3]])
        return f"Conversation with {participant_usernames}{' and others' if self.participants.count() > 3 else ''}"


class Message(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        return f"Message from {self.sender.username}"
