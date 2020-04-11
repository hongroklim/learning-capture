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
    
    path('lecture/create', views.leccreate.as_view(), name='leccreate'),
    
    path('lecture/<int:chapter>', views.leclist.as_view(), name='leclist'),
    
    path('lecture/detail/<int:pk>', views.lecdetail.as_view(), name='lecdetail'),
    
    path('lecture/delete/<int:pk>', views.lecdelete.as_view(), name='lecdelete'),
    
    path('lecture/update/<int:pk>', views.lecupdate.as_view(), name='lecupdate'),
    
]