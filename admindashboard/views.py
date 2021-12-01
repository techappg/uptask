from django.http import HttpResponse
from django.shortcuts import render,redirect
from taskapp.models import *
from admindashboard.forms import UserCreationForm,ProgrammingLanguageForm,TaskTypeForm,SystemDetailForm
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
    print(data)
    print(request.user.is_superuser)
    if request.method=='POST':
      form = UserCreationForm(request.POST)
      print(form)
      if form.is_valid():
          first_name=request.POST["first_name"]
          last_name=request.POST["last_name"]
          username=request.POST["username"]
          password1=request.POST["password1"]
          password2=request.POST["password2"]
          email=request.POST["email"]
          phone_number=request.POST["phone_number"]
          office_user_id=request.POST["office_user_id"]
          reporting_to=request.POST["reporting_to"]
          programming_language=request.POST["programming_language"]
          f1=form.save()
          f1.first_name=first_name
          f1.last_name=last_name
          f1.username=username
          f1.password1=password1
          f1.password2=password2
          f1.email=email
          f1.phone_nmuber=phone_number
          f1.office_user_id=office_user_id
          f1.reporting_to=reporting_to
          f1.is_employee=True
          f1.save()
          added=True
    else:
            form=UserCreationForm(request.POST)
    return render(request,"admindashboard/add_new_user.html",locals())


def view_all_users(request):
    view_user=User.objects.all()
    data = ProgrammingLanguage.objects.all()
    return render (request,"admindashboard/view_all_user.html",locals())

def update_user(request,id):
    ProgrammingLanguage_data = ProgrammingLanguage.objects.all()
    user=User.objects.get(id=id)
    print(user.id)
    if request.method=="POST":
        user.first_name = request.POST["first_name"]
        print( user.first_name )
        user.last_name = request.POST["last_name"]
        user.username = request.POST["username"]
        user.password1 = request.POST["password1"]
        user.email = request.POST["email"]
        user.phone_number = request.POST["phone_number"]
        user.office_user_id = request.POST["office_user_id"]
        user.programming_language_id = request.POST["programming_language"]
        user.reporting_to = request.POST["reporting_to"]
        user.save()
    return render(request,"admindashboard/update_user.html",locals())



def delete_user(request,id):
      user=User.objects.get(id=id)
      user.delete()
      return render (request,"admindashboard/add_new_user.html",locals())



def view_single_user(request,id):
        ProgrammingLanguage_data = ProgrammingLanguage.objects.all()
        user = User.objects.get(id=id)
        print(user)
        return render(request,"admindashboard/view_single_user.html", locals())




def add_programming_language(request):
    if request.method=="POST":
        form = ProgrammingLanguageForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            added=True
    else:
        form =ProgrammingLanguageForm(request.POST)
    return render(request, "admindashboard/add_programming_language.html", locals())

def view_all_programming_language(request):
    view_language=ProgrammingLanguage.objects.all()

    return render(request,"admindashboard/view_all_language.html",locals())


def update_programming_language(request,id):
    language= ProgrammingLanguage.objects.get(id=id)
    print(language.id)
    if request.method == "POST":
        language.language_name = request.POST["language_name"]
        language.is_active = request.POST["is_active"]
        language.save()
    return render(request, "admindashboard/update_programming_language.html", locals())


def delete_programming_language(request,id):
    language = ProgrammingLanguage.objects.get(id=id)
    language.delete()
    return render (request,"admindashboard/add_programming_language.html",locals())


def add_new_task_type(request):
    data = ProgrammingLanguage.objects.all()
    print(data)
    if request.method == 'POST':
        form = TaskTypeForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            added=True
    else:
        form =TaskTypeForm(request.POST)
    return render(request, "admindashboard/add_new_task_type.html", locals())


def view_all_tasktype(request):
    view_type_name=TaskType.objects.all()

    return render(request,"admindashboard/view_all_task_type.html",locals())


def update_task_type(request,id):
    ProgrammingLanguage_data = ProgrammingLanguage.objects.all()
    view_type_name=TaskType.objects.get(id=id)
    print(view_type_name.id)
    if request.method == "POST":
        view_type_name.type_name = request.POST["type_name"]
        view_type_name.is_active = request.POST["is_active"]
        view_type_name.for_all = request.POST["for_all"]
        view_type_name.programming_language_id = request.POST["programming_language"]
        view_type_name.save()
    return render(request, "admindashboard/update_task_type.html", locals())

def delete_task_type(request,id):
    tasktype=TaskType.objects.get(id=id)
    tasktype.delete()

    return render (request,"admindashboard/add_new_task_type.html",locals())

def add_system_details(request):
    if request.method == 'POST':
        form = SystemDetailForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            added=True
    else:
        form = SystemDetailForm(request.POST)
    return render(request, "admindashboard/add_system_detail.html", locals())


def view_all_system_details(request):
    systemdetail=system_detail.objects.all()
    return render (request,"admindashboard/view_all_system_detail.html",locals())


def update_system_details(request,pk):
    systemdetail=system_detail.objects.get(pk=pk)

    print(systemdetail.system_type)
    if request.method == "POST":
        systemdetail.system_type= request.POST["system_type"]
        systemdetail.specification = request.POST["specification"]
        systemdetail.system_service = request.POST["system_service"]
        systemdetail.system_id = request.POST["system_id"]
        systemdetail.added_on = request.POST["added_on"]
        systemdetail.save()
    return render(request, "admindashboard/update_system_detail.html", locals())

def delete_system_details(request,pk):
     systemdetail=system_detail.objects.get(pk=pk)
     print(systemdetail.pk)
     systemdetail.delete()
     return render(request, "admindashboard/add_system_detail.html", locals())


def view_single_system_details(request,pk):
        systemdetail= system_detail.objects.get(pk=pk)
        print(systemdetail)
        return render(request,"admindashboard/view_single_system_detail.html", locals())