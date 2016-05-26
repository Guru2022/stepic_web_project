from django.shortcuts import render
from django.http import Http404

from django.http import HttpResponse
from django.http import Http404

from models import Question
from models import paginate


def questions_list_all(request):
    questions = Question.objects.all()
    page = paginate(request, questions)
    return render(request, 'question_all.html', {
        'posts': page.object_list,
        'paginator': page.paginator,
        'page': page
    })

def questions_list_popular(request):
    questions = Question.objects.popular()
    page = paginate(request, questions)
    return render(request, 'question_all.html', {
        'posts': page.object_list,
        'paginator': page.paginator,
        'page': page
    })

# TODO
def show_question(request):
    pass

def test(request, *args, **kwargs):
    return HttpResponse('OK')
