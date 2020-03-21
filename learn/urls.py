from django.urls import path

from . import views

# namespace for url
app_name = 'learn'
urlpatterns = [    
    path('', views.classrooms.as_view(), name='classrooms'),
]