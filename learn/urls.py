from django.urls import path

from . import views

# namespace for url
app_name = 'learn'
urlpatterns = [
    path('', views.classrooms.as_view(), name='classrooms'),
    
    path('<int:classroom>/', views.weeklyclasses.as_view(), name='weeklyclasses'),
    
    path('chapter/', views.chapter.as_view(), name='chapter'),
]