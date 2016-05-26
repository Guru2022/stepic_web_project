from django.shortcuts import render
from django.http import Http404

from django.http import HttpResponse
from django.http import Http404

from models import Question
from models import Answer
from models import paginate

from forms import AskForm
from forms import AnswerForm


def questions_list_all(request):
    questions = Question.objects.new()
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

def show_question(request, *args):
    try:
        question = Question.objects.get(id=int(args[0]))
    except:
        raise Http404
    answers = Answer.objects.filter(question__id=int(args[0]))
    return render(request, 'answers_all.html', {
        'answers': answers,
        'question': question
    })

def add_question(request, *args):
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            question = form.save()
            return HttpResponseRedirect(question.get_url())
    else:
        form = AskForm()
    return render(request, 'form_template.html', {'form': form)


def test(request):
    return HttpResponse('OK')
