from django.forms import ModelForm
from django import forms
from models import Question
from models import Answer

class AskForm(ModelForm):
    class Meta:
        model=Question
        fields=['title', 'text']

class AnswerForm(ModelForm):
    question = forms.ModelChoiceField(queryset=Question.objects.all(), widget=forms.HiddenInput())

    class Meta:
        model=Answer
        fields=['text', 'question']
