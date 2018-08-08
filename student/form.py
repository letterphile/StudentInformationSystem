from django.forms import ModelForm
from .models import Student

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