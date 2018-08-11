from django.forms import ModelForm
from .models import * 
from django import forms
from django.forms import ModelForm
class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['name','roll_no','batch','branch','current_semester']
class FilterForm(forms.Form):
    semester_list = [(s.semester_code,s.semester_name) for s in CurrentSemester.objects.all()]
    semester_list = [('','ALL')]+semester_list
    branch_list = [(b.branch_code,b.branch_name) for b in Branch.objects.all()]
    branch_list= [('','ALL')]+branch_list
    batch_list = [(bat.year,bat.year) for bat in Batch.objects.all()]
    batch_list = [('','ALL')]+batch_list
    batch = forms.ChoiceField(choices=batch_list,required=False)
    branch = forms.ChoiceField(choices=branch_list,required=False)
    semester = forms.ChoiceField(choices=semester_list,required=False)

class CourseForm(forms.Form):
    course_name = forms.CharField(max_length=50,required=True)
    course_code = forms.CharField(max_length=10,required=True)
    BRA_CHOICES = (('CSE','Computer Science and Engineering'),('EEE','Electrical and Electronics Engineering'),
    ('ECE','Electronics and Communication Engineering'))
    SEMESTERS = (('S1','semester-1'),('S2','semester-2'),('S3','semester-3'),('S4','semester-4'),('S5','semester-4'),
    ('S6','semester-6'),('S7','semester-7'),('S8','semester-8'))
    branch = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=BRA_CHOICES,required=True)
    semester = forms.ChoiceField(choices=SEMESTERS,required=True)