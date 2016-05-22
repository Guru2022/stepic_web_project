from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class QuestionManager(models.Manager):
    def new():
        pass
    def popular():
        pass

class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(null=True)
    rating = models.IntegerField(null=True)
    author = models.ForeignKey(User, related_name='+')
    likes = models.ManyToManyField(User)

    class Meta:
        db_table = 'qadb'

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(null=True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User)

    class Meta:
        db_table = 'qadb'
