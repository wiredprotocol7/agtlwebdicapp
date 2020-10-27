from django.db import models
from django.db.models import Manager
from django.utils import timezone
from django.conf import settings


class Word(models.Model):
    title = models.CharField(max_length=100, primary_key=True, unique=True)
    createdword = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class comment(models.Model):
    word = models.ForeignKey(Word, on_delete=models.CASCADE, related_name='comments')
    objects = models.Manager()
    body = models.TextField(unique=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return ' {} '.format(self.body)
