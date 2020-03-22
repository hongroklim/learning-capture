from django.shortcuts import render, resolve_url, redirect, get_object_or_404, get_list_or_404
from django.views.generic import ListView, DetailView

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


class chapters(ListView):
    model = Chapter
    template_name = 'learn/chapters.html'
    
    def get_queryset(self):
        return Chapter.objects.filter(weeklyclass__pk=self.kwargs['weeklyclass']).order_by('num')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['classroom'] = get_object_or_404(ClassRoom, pk=self.kwargs['classroom'])
        context['weeklyclass'] = get_object_or_404(WeeklyClass, pk=self.kwargs['weeklyclass'])
        return context
    
    
class chapter(DetailView):
    model = Chapter
    template_name = 'learn/chapter.html'
    context_object_name = 'chapter'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['classroom'] = get_object_or_404(ClassRoom, pk=self.kwargs['classroom'])
        context['weeklyclass'] = get_object_or_404(WeeklyClass, pk=self.kwargs['weeklyclass'])
        context['chapters'] = get_list_or_404(Chapter.objects.filter(weeklyclass__pk=self.kwargs['weeklyclass']).order_by('num'))
        return context