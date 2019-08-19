from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.shortcuts import redirect

from .models import Question, Choice
from .forms import QuestionForm, QuestionEditForm

import csv
# Create your views here.


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        '''Return the last five published questions...'''
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


class EditView(generic.edit.UpdateView):
    model = QuestionEditForm
    template_name = 'polls/edit.html'


def question_edit(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.method == 'POST':
        form = QuestionEditForm(request.POST, instance=post)
        if form.is_valid():
            question = form.save()
            question.save()
            return HttpResponseRedirect(reverse('detail',
                                                args=(product.id,)))
    else:
        form = QuestionEditForm(instance=question)
    return render(request, 'polls/edit.html', {
        'form': form,
        'questtion': question
    })


def add(request):
    if request.method == 'POST':
        obj = Question()
        question = QuestionForm(request.POST, instance=obj)
        if question.is_valid():
            question.save()
        return redirect(to='polls:index')
    params = {
        'form': QuestionForm(),
    }
    return render(request, 'polls/add.html', params)


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'question': question,
                                                     'error_message': "You didn't select a choice."})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def download(request):
    response = HttpResponse(content_type='text/csv')
    filename = 'data.csv'
    response['Content-Disposition'] = 'attachment; filename={}'.format(
        filename)
    writer = csv.writer(response)

    questons = Question.objects.order_by('pub_date')
    for question in questons:
        writer.writerow([question.question_text, question.pub_date])
    return response
