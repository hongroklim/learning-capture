from django.db import models
from django.urls import reverse
from ELearningPy.settings import MEDIA_ROOT
import os

#TODO : INTEGER RANGE

#from django.db.models import IntegerField, Model
#from django.core.validators import MaxValueValidator, MinValueValidator
#class CoolModelBro(Model):
#    limited_integer_field = IntegerField(
#        default=1,
#        validators=[
#            MaxValueValidator(100),
#            MinValueValidator(1)
#        ]
#     )

#강의
class ClassRoom(models.Model):
    year = models.IntegerField()
    semester = models.IntegerField()
    title = models.CharField(max_length=50)
    professor = models.CharField(max_length=20, blank=True)
    opendate = models.CharField(max_length=8, blank=True)
    closedate = models.CharField(max_length=8, blank=True)
    
    def __str__(self):
        return '%d-%d : %s' % (self.year, self.semester, self.title)

    
#주차별 강의
class WeeklyClass(models.Model):
    classroom = models.ForeignKey(ClassRoom, on_delete = models.CASCADE)
    num = models.IntegerField()
    title = models.CharField(max_length=50, blank=True)
    
    def __str__(self):
        return '%d : %s' % (self.num, self.title)

    
#단원
class Chapter(models.Model):
    weeklyclass = models.ForeignKey(WeeklyClass, on_delete = models.CASCADE)
    num = models.IntegerField()
    title = models.CharField(max_length=50, blank=True)
    videolink = models.URLField(max_length=200, blank=True)
    video = models.FileField(upload_to="learn/videos", blank=True)
    
    def __str__(self):
        return '%d : %s (%d) <%s>' % (self.weeklyclass.num, self.weeklyclass.title, self.num, self.title)
    

#수업
class Lecture(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete = models.CASCADE)
    num = models.IntegerField(default=0)
    image = models.ImageField(upload_to="learn/images/lecture", blank=True)
    title = models.CharField(max_length=50, blank=True)
    note = models.TextField(max_length=500, blank=True)
    
    def __str__(self):
        return '%d-%d-%d-%d : %s' % (self.chapter.weeklyclass.classroom.pk, self.chapter.weeklyclass.num, self.chapter.num, self.num, self.title)
    
    def get_absolute_url(self):
        param = [self.chapter.weeklyclass.classroom.pk, self.chapter.weeklyclass.pk, self.chapter.pk]
        return reverse('learn:chapter', args=param)
    
    def delete(self, *args, **kargs):
        os.remove(os.path.join(MEDIA_ROOT, self.image.path))
        super(Lecture, self).delete(*args, **kargs)