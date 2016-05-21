from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Question(models):
    title = models.CharField()
    text = models.TextField()
    added_at = models.DateField()
    rating = models.DecimalField()
    author = models.OneToOneField(User)
    likes = models.ManyToManyField(User)

class Answer(models):
    text = models.TextField()
    added_at = models.DateField()
    question = models.ForeignKey(Question)
    author = models.OneToOneField(User)
