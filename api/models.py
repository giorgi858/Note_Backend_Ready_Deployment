from django.db import models
from django.contrib.auth.models import User
import uuid

class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    content = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    
    def __str__(self) :
        return f'{self.content[0:50]} by {self.author.username}'
    