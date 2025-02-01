from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Tag(models.Model):
    """Tag model to categorize snippets by a unique title."""
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title


class Snippet(models.Model):
    """Snippet model for storing short text notes, each associated with one tag."""
    note = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return self.note
