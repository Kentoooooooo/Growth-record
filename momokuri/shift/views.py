from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import Submit


class ShiftListView(ListView):
    model = Submit
    template_name = 'shift/shift_list.html'

    def queryset(self):
        return Submit.objects.all()
