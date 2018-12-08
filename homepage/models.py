from django.db import models
from accounts.models import User

# Create your models here.


class Friendship(models.Model):
    sender = models.ForeignKey(User, related_name="senderFriend", on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name="receiverFriend", on_delete=models.CASCADE)
    sendTime = models.DateTimeField()
    status = models.TextField(max_length=20)
