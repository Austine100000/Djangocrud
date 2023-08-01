from django.shortcuts import render, redirect
from new.models import student
from new.forms import studentForm


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = studentForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = studentForm()
        return render(request, 'index.html', {'form': form})


def show(request):
    students = student.objects.all()
    return render(request, 'show.html', {'students': students})


def edit(request, id):
    students = student.objects.get(id=id)
    return render(request, 'edit.html', {'student': students})


def delete(request, id):
    students = student.objects.get(id=id)
    students.delete()
    return redirect('/show')


def update(request, id):
    students = student.objects.get(id=id)
    form = studentForm(request.POST, instance=students)
    if form.is_valid():
        form.save()
        return redirect('/show')
    else:
        return render(request, 'edit.html', {'student': students})
