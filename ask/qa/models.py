from __future__ import unicode_literals

from django.db import models

# Create your models here.

Class Question(models):
    title = models.CharField()
    text = models.TextField()
    added_at = models.DateField()
    rating = models.DecimalField()
    author = models.ForeignKey('Author')
    likes = models.ManyToManyField('Author')
