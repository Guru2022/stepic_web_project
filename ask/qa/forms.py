from django.forms import ModelForm
from qa.models import Question
from qa.models import Answer

class AskForm(ModelForm):
    class Meta:
        model=Question
        fields=['title', 'text']

class AnswerForm(ModelForm):
    class Meta:
        model=Answer
        fields=['text', 'question']
