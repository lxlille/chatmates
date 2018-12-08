from django.db import models
from accounts.models import User

import django.utils.timezone


class Discussion(models.Model):
    discussionNumber = models.PositiveIntegerField(default=0)
    createrUser = models.ForeignKey(User, on_delete=models.CASCADE, default=User.get_username)


class DiscussionMessage(models.Model):
    discussion = models.ForeignKey(Discussion, related_name="messages", on_delete=models.CASCADE)
    time = models.DateTimeField(default=django.utils.timezone.now)
    sender = models.ForeignKey(User, related_name="sender", on_delete=models.CASCADE)
    messageData = models.CharField(max_length=255)

    class Meta:
        ordering = ["-time"]


class DiscussionMember(models.Model):
    discussion = models.ForeignKey(Discussion, related_name="users", on_delete=models.CASCADE)
    member = models.ForeignKey(User, on_delete=models.CASCADE)
