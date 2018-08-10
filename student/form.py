from django.forms import ModelForm
from .models import Student
from django import forms

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['name','roll_no','semester','branch','batch']
class FilterForm(ModelForm):
    class Meta:
        model = Student
        fields = [
            'batch','branch','semester'
        ]

class CourseForm(forms.Form):
    course_name = forms.CharField(max_length=50,required=True)
    course_code = forms.CharField(max_length=10,required=True)
    BRA_CHOICES = (('CSE','Computer Science and Engineering'),('EEE','Electrical and Electronics Engineering'),
    ('ECE','Electronics and Communication Engineering'))
    SEMESTERS = (('S1','semester-1'),('S2','semester-2'),('S3','semester-3'),('S4','semester-4'),('S5','semester-4'),
    ('S6','semester-6'),('S7','semester-7'),('S8','semester-8'))
    branch = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=BRA_CHOICES,required=True)
    semester = forms.ChoiceField(choices=SEMESTERS,required=True)
