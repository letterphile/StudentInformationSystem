from django.shortcuts import render
from .form import StudentForm,FilterForm
from .models import *
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
def student_form(request,student_id):
    if request.method == 'POST':
        stud = Student.objects.get(id=student_id)
        result_list = []
        try:
            for i in ['name','roll_no','semester','branch','batch']:
                result_list.append(request.POST[i])
        except KeyError:
            result_list.append(None)
        j=0
        for result in result_list:
            if result != None and  j==0:
                stud.name = result
                print(result)
                stud.save()
            if result != None and j==1:
                stud.roll_no= result
                stud.save()
            if result != None and j==2:
                try:
                    stud.semester.remove(Semester.objects.get(id=stud.semester.get().id))
                    stud.semester.add(Semester.objects.get(id=result))
                    stud.save()
                except ObjectDoesNotExist:
                    stud.semester.add(Semester.objects.get(id=result))
                    stud.save()
            if result != None and j==3:
                try:
                    stud.branch.remove(Branch.objects.get(id=stud.branch.get().id))
                    stud.branch.add(Branch.objects.get(id=result))
                    stud.save()
                except ObjectDoesNotExist:
                    stud.branch.add(Branch.objects.get(id=result))
                    stud.save()
            if result != None and j==4:
                try:
                    stud.batch.remove(Batch.objects.get(id=stud.batch.get().id))
                    stud.batch.add(Batch.objects.get(id=result))
                    stud.save()
                except ObjectDoesNotExist:
                    stud.batch.add(Batch.objects.get(id=result))
                    stud.save()
            j+=1
        stud.save()
        std = Student.objects.get(id=student_id) 
        my_form = StudentForm(instance=std)
    else:                
        std = Student.objects.get(id=student_id)
        my_form = StudentForm(instance=std)
    return render(request,'student/detail_form.html',{'form':my_form,'std':std})

def filter_form(request):
    f_form = FilterForm()
    return render(request,'student/form.html',{'form':f_form})
def show_result(request):
    students = Student.objects.all()
    result_list = []
    result_list.append(request.POST.get('batch'))
    result_list.append(request.POST.get('semester'))
    result_list.append(request.POST.get('branch'))
    i=0
    for result in result_list:
        if result != None and i == 0 :
            bat= Batch.objects.get(id=result)
            students = students.filter(batch=bat)
        if result != None and i==1 :
            sem= Semester.objects.get(id=result)
            students = students.filter(semester=sem)
        if result != None and i==2:
            bra = Branch.objects.get(id=result) 
            students = students.filter(branch=bra)
        i+=1
    
    return render(request,'student/result.html',{'students':students})
def student_add(request):
    if request.method=='POST':
        result_list =[]
        try:
            for i in ['name','roll_no','semester','branch','batch']:
                result_list.append(request.POST[i])
        except KeyError:
            result_list.append(None)
        j=0
        stud = Student()
        for result in result_list:
            if result != None and  j==0:
                stud.name = result
                print(result)
            if result != None and j==1:
                stud.roll_no= result
                stud.save()
            if result != None and j==2:
                try:
                    stud.semester.add(Semester.objects.get(id=result))
                    stud.save()
                except ObjectDoesNotExist:
                    stud.semester.add(Semester.objects.get(id=result))
                    stud.save()
            if result != None and j==3:
                try:
                    stud.branch.add(Branch.objects.get(id=result))
                    stud.save()
                except ObjectDoesNotExist:
                    stud.branch.add(Branch.objects.get(id=result))
                    stud.save()
            if result != None and j==4:
                try:
                    stud.batch.add(Batch.objects.get(id=result))
                    stud.save()
                except ObjectDoesNotExist:
                    stud.batch.add(Batch.objects.get(id=result))
                    stud.save()
            j+=1
        add_form = 'Empty'
        

    else:
        add_form = StudentForm()
        stud = 'empty'
        
    return render(request,'student/add_form.html',{'add_form':add_form,'stud':stud}) 

def student_delete(request,student_id):
    std = Student.objects.get(id=student_id)
    name = std.name
    id = std.id
    std.delete()
    return render(request,'student/base.html',{'name':name,'id':id})
def student_view(request,student_id):
    std = Student.objects.get(id=student_id)
    batch_len = len(std.batch.all())
    bra_len = len(std.branch.all())
    semester_len = len(std.semester.all())
    return render(request,'student/view.html',{'std':std,'batch_len':batch_len,'bra_len':bra_len,'sem_len':semester_len})
def view_students(request):
    students = Student.objects.all()
    return render(request,'student/view_result.html',{'students':students})
    