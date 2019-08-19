from django import forms

from polls.models import Question, Choice


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('question_text',)


class QuestionEditForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('question_text',)
