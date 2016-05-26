from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.core.paginator import Paginator

# function helper
def paginate(request, qs):
    try:
        limit = int(request.GET.get('limit', 10))
    except ValueError:
        limit = 10
    if limit > 100:
        limit = 10
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    paginator = Paginator(qs, limit)
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return page

# Create your models here.

class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-added_at')

    def popular(self):
        return self.order_by('-rating')

class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True, null=True)
    rating = models.IntegerField(null=True, default=0)
    author = models.ForeignKey(User, related_name='+', null=True, blank=True)
    likes = models.ManyToManyField(User)

    def get_url(self):
        return "/question/%d/" % self.id

    class Meta:
        db_table = 'question'

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(null=True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User, null=True, blank=True)

    class Meta:
        db_table = 'answer'
