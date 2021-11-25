from django.http import HttpResponse
from django.shortcuts import render,redirect
from taskapp.models import *
from admindashboard.forms import UserCreationForm,ProgrammingLanguageForm
def all_users(request,layout=None):
    all_users_admin_data=User.objects.filter(is_superuser=True)
    all_employees_data=User.objects.filter(is_superuser=False)
    if layout is None:
        return render(request,"admindashboard/all_users_table_layout.html",locals())

    if layout =="tabular":
        return render(request,"admindashboard/all_users_table_layout.html",locals())
    if layout =="grid":
        return render(request,"admindashboard/all_users_grid_layout.html",locals())


def add_new_user(request):
    data = ProgrammingLanguage.objects.all()
    print(request.user.is_superuser)
    if(request.user.is_superuser)=="True":
      if request.method=='POST':
          form = UserCreationForm(request.POST)
          if form.is_valid():
           form.save()

    else:
            form=UserCreationForm(request.POST)
    return render(request,"admindashboard/add_new_user.html", locals())


def view_all_users(request):
    view_user=User.objects.all()
    return render (request,"admindashboard/view_all_user.html",locals())


def add_programming_language(request):
    if request.method=="POST":
        form = ProgrammingLanguageForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
    else:
        form =ProgrammingLanguageForm(request.POST)
    return render(request, "admindashboard/add_programming_language.html", locals())

def view_all_programming_language(request):
    view_language=ProgrammingLanguage.objects.all()

    return render(request,"admindashboard/view_all_language.html",locals())