from django.db import models
from .rosteruser import RosterUser
import uuid


class SharedCharacterToken(models.Model):
    token = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    user = models.ForeignKey(RosterUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.user.user.username} - {self.token}'
