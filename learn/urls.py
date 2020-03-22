from django.urls import path, re_path

from . import views

# namespace for url
app_name = 'learn'
urlpatterns = [
    path('', views.classrooms.as_view(), name='classrooms'),
    
    path('<int:classroom>/', views.weeklyclasses.as_view(), name='weeklyclasses'),
    
    path('<int:classroom>/<int:weeklyclass>/', views.chapters.as_view(), name='chapters'),
    
    re_path(r'^(?P<classroom>\d+)/(?P<weeklyclass>\d+)/(?P<pk>\d+)/(?:(?P<lecture>\d+/))?$',
            views.chapter.as_view(),
            name='chapter'),
    
]