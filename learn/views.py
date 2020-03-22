from django.shortcuts import render, resolve_url, redirect, get_object_or_404, get_list_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from django.core.serializers import serialize

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
        try:
            context['lectures'] = Lecture.objects.filter(chapter__pk=self.kwargs['pk']).order_by('num', 'pk')
        except Lecture.DoesNotExist:
            context['lectures'] = None;
        
        return context

    
#Mixin to add AJAX support to a form.
#Must be used with an object-based FormView (e.g. CreateView)
class LectureAjaxResponseMixin:
    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response


class leccreate(LectureAjaxResponseMixin, CreateView):
    model = Lecture
    fields = ['chapter', 'num', 'image', 'title', 'note']
    
    def form_valid(self, form):
        response = super().form_valid(form)
        #return할 때 자기가 이 chapter에서 몇 번째 lecture인지 알려줌.
        #length
        #index
        data = {
            'lectureLength': Lecture.objects.filter(chapter__pk=self.object.chapter.pk).count(),
            'lectureIndex': Lecture.objects.filter(chapter__pk=self.object.chapter.pk, num__lte=self.object.num).count(),
            'lecturePk': self.object.pk
        }
        return JsonResponse(data)


class leclist(ListView):
    model = Lecture
    
    def get_queryset(self):
        return Lecture.objects.filter(chapter__pk=self.kwargs['chapter']).order_by('num', 'pk')
    
    def render_to_response(self, context, **response_kwargs):
        data = serialize('json', self.get_queryset())
        return JsonResponse(data, safe=False, **response_kwargs)

class lecdetail(DetailView):
    model = Lecture
    
    def get_queryset(self):
        return get_object_or_404(Lecture, pk=self.kwargs['pk'])
    
    def render_to_response(self, context, **response_kwargs):
        data = serialize('json', self.get_queryset())
        return JsonResponse(data, safe=False, **response_kwargs)