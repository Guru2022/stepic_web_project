from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.http import Http404

from django.http import HttpResponseRedirect
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

@csrf_protect
def show_question(request, *args):
    try:
        question = Question.objects.get(id=int(args[0]))
    except:
        raise Http404

    answers = Answer.objects.filter(question__id=int(args[0]))
    form = AnswerForm(initial={'question':question,})
    return render(request, 'answers_all.html', {
        'answers': answers,
        'question': question,
        'form': form
    })

@csrf_protect
def add_question(request):
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(form.save().get_url())
    else:
        form = AskForm()
    return render(request, 'form_template.html', {'form': form})

@csrf_protect
def add_answer(request):
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(form.cleaned_data.get('question').get_url())
    else:
        return HttpResponseRedirect('/')
    return render(request, 'form_template.html', {'form': form})

def test(request):
    return HttpResponse('OK')
