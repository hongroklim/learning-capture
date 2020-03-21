from django.shortcuts import render, resolve_url, redirect, get_object_or_404
from django.views.generic import ListView, TemplateView

from learn.models import *

class classrooms(ListView):
    model = ClassRoom
    template_name = 'learn/classrooms.html'

class weeklyclasses(ListView):
    model = WeeklyClass
    template_name = 'learn/weeklyclasses.html'

    def get_queryset(self):
        return WeeklyClass.objects.filter(classroom__pk=self.kwargs['classroom']).order_by('num')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['classroom'] = get_object_or_404(ClassRoom, pk=self.kwargs['classroom'])
        return context

class chapter(TemplateView):
    template_name = 'learn/chapter.html'