from django.shortcuts import render, resolve_url, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
#from django import forms

from learn.models import *

class classrooms(ListView):
    model = ClassRoom
    template_name = 'learn/classrooms.html'