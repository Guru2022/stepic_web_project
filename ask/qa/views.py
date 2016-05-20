from django.shortcuts import render
from django.http import Http404

from django.http import HttpResponse
def test(request, *args, **kwargs):
    return HttpResponse('OK')
