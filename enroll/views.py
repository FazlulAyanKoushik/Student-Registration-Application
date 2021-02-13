from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student

# Create your views here.
def add_show(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form = form.save(commit = False)
            form.save()
            form = StudentForm()
    else:
        form = StudentForm()
    all_student = Student.objects.all()
    return render(request, 'enroll/addandshow.html', {'form':form, 'stud': all_student})

#edit data
def edit_data(request, id):
    if request.method == 'POST':
        pi = Student.objects.get(pk = id)
        form = StudentForm(request.POST, instance = pi)   
        if form.is_valid():
            form.save() 
            return redirect('/')
    else:
        pi = Student.objects.get(pk = id)
        form = StudentForm(instance = pi)
    return render(request, 'enroll/updatestudent.html', {'form':form})

#delete data
def delete_data(request, id):
    if request.method == "POST":
        pi = Student.objects.get(pk = id)
        pi.delete()
        return redirect('/')