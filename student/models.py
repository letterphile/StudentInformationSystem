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
    
class Semester(models.Model):
    semester_name = models.CharField(max_length = 10)
    semester_code = models.CharField(max_length = 2)
    status = models.CharField(max_length=10,choices=(('current','Current'),('past','Past'),),default='current',blank=True)
    branch = models.ManyToManyField(Branch) 
    class Meta:
        ordering = ('semester_code',)
    def __str__(self):
        return self.semester_name

class Course(models.Model):
    course_name = models.CharField(max_length= 45)
    course_code = models.CharField(max_length=7)
    semester = models.ManyToManyField(Semester)
    branch = models.ManyToManyField(Branch)

    class Meta:
        ordering = ('course_code',)
    def __str__(self):
        return self.course_name
    
class Grade(models.Model):
    grade_value = models.CharField(max_length=2)
    course = models.ManyToManyField(Course)
    
    
    class Meta:
        ordering = ('grade_value',)
    def __str__(self):
        return self.grade_value

class Student(models.Model):
    name = models.CharField(max_length=15)
    roll_no = models.PositiveIntegerField()
    course = models.ManyToManyField(Course)
    grade= models.ManyToManyField(Grade)
    batch = models.ManyToManyField(Batch)
    branch = models.ManyToManyField(Branch)
    semester = models.ManyToManyField(Semester)
    objects = models.Manager()
    class Meta :
        ordering = ('name',)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('student:student_form',args=[
            self.id,
        ])
