from django.forms import ModelForm
from models import Question
from models import Answer

class AskForm(ModelForm):
    class Meta:
        model=Question
        fields=['title', 'text']

class AnswerForm(ModelForm):
    class Meta:
        model=Answer
        fields=['text', 'question']
