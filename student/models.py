from django.db import models
from django.urls import reverse
# Create your models here.
class Batch(models.Model):
    year = models.PositiveIntegerField()
    class Meta:
        ordering = ('year',)
    def __str__(self):
        return str(self.year)
class Branch(models.Model):
    branch_name= models.CharField(max_length=25)
    branch_code = models.CharField(max_length=3)
    class Meta:
        ordering =  ('branch_name',)
    def __str__(self):
        return self.branch_name
class CurrentSemester(models.Model):
    semester_name = models.CharField(max_length = 10)
    semester_code = models.CharField(max_length = 2)
    branch = models.ManyToManyField(Branch) 
    class Meta:
        ordering = ('semester_code',)
    def __str__(self):
        return self.semester_name
class PastSemester(models.Model):
    semester_name = models.CharField(max_length = 10)
    semester_code = models.CharField(max_length = 2)
    branch = models.ManyToManyField(Branch) 
    class Meta:
        ordering = ('semester_code',)
    def __str__(self):
        return self.semester_name
class Grade(models.Model):
    GRADES = [(x,x) for x in ['O','A+','A','B+','B','C+','C','P','F','FE']]
    grade = models.CharField(max_length=2,choices = GRADES)
    class Meta:
        ordering = ('id',)
    def __str__(self):
        return self.grade
class InternalMark(models.Model):
    mark = models.PositiveSmallIntegerField()
    class Meta:
        ordering=('mark',)
    def __str__(self):
        return str(self.mark)

class Attendance(models.Model):
    attendance = models.PositiveSmallIntegerField()
    class Meta:
        ordering = ('attendance',)
    def __str__(self):
        return str(self.attendance)

class Course(models.Model):
    course_name = models.CharField(max_length= 45)
    course_code = models.CharField(max_length=7)
    semester = models.ForeignKey(CurrentSemester,on_delete=models.CASCADE)
    branch = models.ManyToManyField(Branch)
    grade = models.ManyToManyField(Grade)

    class Meta:
        ordering = ('id',)
    def __str__(self):
        return self.course_name
class Student(models.Model):
    name = models.CharField(max_length=15)
    roll_no = models.PositiveIntegerField()
    course = models.ManyToManyField(Course)
    grade_list = []
    attendance_list =[]
    internalmark_list = []
    batch = models.ForeignKey(Batch,on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE)
    current_semester = models.ForeignKey(CurrentSemester,on_delete=models.CASCADE)
    past_semester= models.ManyToManyField(PastSemester)
    objects = models.Manager()
    class Meta :
        ordering = ('name',)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('student:student_form',args=[
            self.id,
        ])