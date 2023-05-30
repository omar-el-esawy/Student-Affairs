from multiprocessing import context
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import NameForm, Student
from django.urls import reverse


def index(request):
    return render(request, 'pages/mainPage.html')


def search(request):
    return render(request, 'pages/search.html')


# def searchResult(request):
#     context = {
#         'students': Student.objects.all()
#     }
#     return render(request, 'pages/searchResult.html', context)


def searchResult(request):
    search = Student.objects.all()  # Search results should be related by students
    name = None
    if 'search_name' in request.GET:  # If I get search_name in get request.
        # return the same thing (value)..ex:If i write o,return o.
        name = request.GET['search_name']
        if name:
            search = search.filter(name__icontains=name)
    context = {
        'students': search,
    }
    return render(request, 'pages/searchResult.html', context)


def add(request):
    if request.method == 'POST':

        form = NameForm(request.POST)

        if form.is_valid():
            print("it works")
            form.save()

    context = {
        'data': NameForm(),
    }
    return render(request, 'pages/addPage.html', context)
# 01001776648


def active(request):
    forms = NameForm()
    # fromslist = ', '.join([F.status for F in forms])
    context = {
        'students': Student.objects.all(),
        # 'forms': fromslist
    }
    return render(request, 'pages/activeInActive.html', context)


def edit(request, id):
    student = Student.objects.get(idenNum=id)

    if request.method == 'POST':
        student_save = NameForm(request.POST, instance=student)

        if student_save.is_valid():
            student_save.save()
            return redirect('/searchresult/')

    else:
        student_save = NameForm(instance=student)

    context = {
        'data': student_save,
        'iddd': student.idenNum,
    }

    return render(request, 'pages/EditPage.html', context)


def dele(request, id):
    student_delete = get_object_or_404(Student, idenNum=id)

    student_delete.delete()
    return redirect('/searchresult/')


def assign(request, id):
    student = Student.objects.get(idenNum=id)

    if request.method == 'POST':
        student_save = NameForm(request.POST, instance=student)

        if student_save.is_valid():
            print("test")
            student_save.save()
            return redirect('/searchresult/')
    else:
        student_save = NameForm(instance=student)

    context = {
        'form': student_save,
        'data': student,
    }

    return render(request, 'pages/assignDep.html', context)


def activeEdit(request, id):
    studentEdit = get_object_or_404(Student, idenNum=id)

    if request.method == 'POST':
        student_save = NameForm(request.POST, instance=studentEdit)

        if student_save.is_valid():
            student_save.save()
            return redirect('/isActive/')
    else:
        student_save = NameForm(instance=studentEdit)

    context = {
        'form': student_save,
        'data': studentEdit,
    }

    return render(request, 'pages/activechange.html', context)


def about(request):
    return render(request, 'pages/about.html')
