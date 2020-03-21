from django.db import models

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
    year = models.IntegerField(null=False)
    semester = models.IntegerField(null=False)
    title = models.CharField(max_length=50, null=True)
    professor = models.CharField(max_length=20, null=True)
    opendate = models.CharField(max_length=8, null=True)
    closedate = models.CharField(max_length=8, null=True)
    
    def __str__(self):
        return '%d-%d : %s' % (self.year, self.semester, self.title)

#주차별 강의
class WeeklyClass(models.Model):
    classroom = models.ForeignKey(ClassRoom, on_delete = models.CASCADE)
    num = models.IntegerField(null=False)
    title = models.CharField(max_length=50, null=True)
    
    def __str__(self):
        return '%d : %s' % (self.num, self.title)

#단원
class Chapter(models.Model):
    weeklyclass = models.ForeignKey(WeeklyClass, on_delete = models.CASCADE)
    num = models.IntegerField(null=False)
    title = models.CharField(max_length=50, null=True)
    
#수업
class Lecture(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete = models.CASCADE)
    order = models.IntegerField(default=99)
    title = models.CharField(max_length=50, null=True)
    note = models.TextField(max_length=500, null=True)
    
    def __str__(self):
        return '%d-%d : %s' % (self.chapter.weeklyclass.num, self.chapter.num, self.title)

#수업 이미지
class LectureImage(models.Model):
    lecture = models.ForeignKey(Lecture, on_delete = models.CASCADE)
    order = models.IntegerField(default=99)
    image = models.ImageField()
    
    def __str__(self):
        return '%s - %d' % (self.lecture.title, self.order)