from django.shortcuts import render
from .form import StudentForm,FilterForm,CourseForm
from .models import *
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
def student_form(request,student_id):
    if request.method == 'POST':
        stud = Student.objects.get(id=student_id)
        result_list = []
        try:
            for i in ['name','roll_no','current_semester','branch','batch']:
                result_list.append(request.POST[i])
        except KeyError:
            result_list.append(None)
        j=0
        for result in result_list:
            if result != None and  j==0:
                stud.name = result
                print(result)
            if result != None and j==1:
                stud.roll_no= result
                stud.save()
            if result != None and j==2:
                    stud.current_semester= CurrentSemester.objects.get(id=result)
                    stud.save()
                    courses = Course.objects.filter(semester=stud.current_semester).filter(branch=stud.branch)
                    stud.course.clear()
                    for course in courses:
                        stud.course.add(course)
            if result != None and j==3:
                    stud.branch =Branch.objects.get(id=result)
                    stud.save()
                    courses = Course.objects.filter(semester=stud.current_semester).filter(branch=stud.branch)
                    stud.course.clear()
                    for course in courses:
                        stud.course.add(course)
            if result != None and j==4:
                    stud.batch = Batch.objects.get(id=result)
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
        if result != '' and i == 0 :
            bat= Batch.objects.get(year=result)
            students = students.filter(batch=bat)
        if result != '' and i==1 :
            sem= CurrentSemester.objects.get(semester_code=result)
            students = students.filter(current_semester=sem)
        if result != '' and i==2:
            bra = Branch.objects.get(branch_code=result) 
            students = students.filter(branch=bra)
        i+=1
    
    return render(request,'student/result.html',{'students':students})
def student_add(request):
    if request.method=='POST':
        result_list =[]
        try:
            for i in ['name','roll_no','current_semester','branch','batch']:
                result_list.append(request.POST[i])
        except KeyError:
            result_list.append(None)
        bat = Batch.objects.get(id=result_list[4])
        csem = CurrentSemester.objects.get(id=result_list[2])
        bra = Branch.objects.get(id=result_list[3])
        stud = Student(name=result_list[0],roll_no=result_list[1],
        current_semester=csem,batch=bat,branch=bra)
        stud.save()
        courses  = Course.objects.filter(semester=stud.current_semester).filter(branch=stud.branch)
        for course in courses:
            stud.course.add(course)
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
    std_sem =std.current_semester
    std_bra =std.branch
    courses = std.course.all()
    batch_name = std.batch.year
    branch_name =  std.branch.branch_name
    sem_name = std.current_semester.semester_name
    return render(request,'student/view.html',{'std':std,
    'branch_name':branch_name,'batch_name':batch_name,'sem_name':sem_name,'courses':courses} )
def view_students(request):
    students = Student.objects.all()
    return render(request,'student/view_result.html',{'students':students})

def course_add(request):
    if request.method=='POST':
        cours = Course(course_name=request.POST.get('course_name'),
        course_code=request.POST.get('course_code'),
        semester=CurrentSemester.objects.get(semester_code=request.POST.get('semester')))
        cours.save()
        for branch in request.POST.getlist('branch'):
            cours.branch.add(Branch.objects.get(branch_code=branch))
            stds= Student.objects.filter(branch=Branch.objects.get(branch_code=branch)).filter(current_semester=CurrentSemester.objects.get(semester_code=request.POST.get('semester')))
            print(stds)
            for std in stds:
                cours.student_set.add(std)
                cours.save()

        cours.save()
        
        cours_form='Empty'
        
    else:
        cours_form = CourseForm()
        cours = 'empty'
        
    return render(request,'student/course_form.html',{'cours_form':cours_form,'cours':cours}) 