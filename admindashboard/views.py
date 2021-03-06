from datetime import datetime

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render,redirect
from taskapp.models import *
from .forms import *
from django.core.exceptions import ValidationError



# def all_users(request):
#     all_users_admin_data=User.objects.filter(is_superuser=True).values()
#     print(all_users_admin_data)
#     return render(request, "admindashboard/view_all_user_admin.html")
    # all_employees_data=User.objects.filter(is_superuser=False)
    # if layout is None:
    #     return render(request,"admindashboard/all_users_table_layout.html",locals())
    #
    # if layout =="tabular":
    #     return render(request,"admindashboard/all_users_table_layout.html",locals())
    # if layout =="grid":
    #     return render(request,"admindashboard/all_users_grid_layout.html",locals())




def add_new_user(request):
    data = ProgrammingLanguage.objects.filter(is_active=True)
    for i in data:
        print(i.language_name)
    if request.method=='POST':
      form = UserCreationForm(request.POST)
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
      if form.is_valid():
          f1=form.save()
          f1.first_name=first_name
          f1.last_name=last_name
          f1.username=username
          f1.password1=password1
          f1.password2=password2
          f1.email=email
          f1.phone_number=phone_number
          f1.office_user_id=office_user_id
          f1.reporting_to=reporting_to
          f1.is_employee=True
          f1.save()
          added=True

      else:
            notadd=True
            form=UserCreationForm(request.POST)
            return render(request,"admindashboard/add_new_user.html",locals())

    else:
        form = UserCreationForm()
    return render(request, "admindashboard/add_new_user.html", locals())

###########################################
def view_all_users(request):
    view_user=User.objects.all()
    data = ProgrammingLanguage.objects.all()
    usertask = Task.objects.all()

    return render (request,"admindashboard/view_all_user.html",locals())

def update_user(request,id):
    ProgrammingLanguage_data = ProgrammingLanguage.objects.all()
    user=User.objects.get(id=id)
    if request.method=="POST":
        user.first_name = request.POST["first_name"]
        user.last_name = request.POST["last_name"]
        user.username = request.POST["username"]
        user.email = request.POST["email"]
        user.phone_number = request.POST["phone_number"]
        user.office_user_id = request.POST["office_user_id"]
        user.programming_language_id = request.POST["programming_language"]
        user.reporting_to = request.POST["reporting_to"]
        user.save()
        added = True
        return redirect("/admin-dashboard/view-all-users/")
    return render(request,"admindashboard/update_user.html",locals())

def delete_user(request,id):
      user=User.objects.get(id=id)
      user.delete()
      return redirect("/admin-dashboard/view-all-users/")




def add_programming_language(request):
    if request.method == "POST":
        form = ProgrammingLanguageForm(request.POST)
        language_name = request.POST["language_name"]
        if form.is_valid():
            f = form.save()
            f.language_name=language_name
            f.save()
            added = True

        else:
            notadd=True
    else:


        form =ProgrammingLanguageForm(request.POST)
    return render(request, "admindashboard/add_programming_language.html", locals())


def view_all_programming_language(request):
    view_language=ProgrammingLanguage.objects.all()

    return render(request,"admindashboard/view_all_language.html",locals())

def update_programming_language(request,id):
    language= ProgrammingLanguage.objects.get(id=id)
    if request.method == "POST":
        language.language_name = request.POST["language_name"]
        language.is_active = request.POST["is_active"]

        language.save()

        added = True
        return redirect("/admin-dashboard/view-all-programming-language/")
    return render(request, "admindashboard/update_programming_language.html", locals())

def delete_programming_language(request,id):
    language = ProgrammingLanguage.objects.get(id=id)
    language.delete()
    return redirect ("/admin-dashboard/view-all-programming-language/")




def add_new_task_type(request):
    data = ProgrammingLanguage.objects.filter(is_active=True)
    if request.method == 'POST':
        form = TaskTypeForm(request.POST)
        print(form)
        if form.is_valid():
            type_name = request.POST['type_name']
            try:
                for_all = request.POST['for_all']
            except:
                for_all = False

            print(for_all)
            created_task_type = TaskType.objects.create(type_name=type_name,for_all=for_all)
            mul_language= TaskType.objects.filter(for_all=False)
            for i in mul_language :
                 i.multiple_language = True
                 i.save()
            added=True
        else:
         notadd = True
         form = TaskTypeForm(request.POST)

         return render(request, "admindashboard/add_new_task_type.html", locals())


        print(request.POST.getlist('programming_language'),"request.POST.getlist('programming_language')")
        for d in request.POST.getlist('programming_language'):
            print(d)
            multiple_select_language.objects.create(task_type_id=created_task_type.pk,programming_language_id=d)


    else:
        form =TaskTypeForm(request.POST)
    return render(request, "admindashboard/add_new_task_type.html", locals())




def view_all_tasktype(request):
  view_type=TaskType.objects.all()
  a = multiple_select_language.objects.all()
  return render(request,"admindashboard/view_all_task_type.html",locals())

def update_task_type(request,id):
    ProgrammingLanguage_data = ProgrammingLanguage.objects.all()
    view_type_name=TaskType.objects.get(id=id)
    if request.method == "POST":
        view_type_name.type_name = request.POST["type_name"]
        view_type_name.for_all = request.POST["for_all"]
        view_type_name.is_active=request.POST["is_active"]
        # print(type(request.POST.get('for_all')),request.POST.get('for_all'))
        if request.POST.get('for_all') == "False":
         view_type_name.programming_language_id = request.POST["programming_language"]
        elif request.POST.get('for_all') == "True":
          view_type_name.programming_language_id =request.POST["programming_language"]
        view_type_name.save()
        added=True
        return redirect("/admin-dashboard/view-all-tasktype/")
    return render(request, "admindashboard/update_task_type.html", locals())

def delete_task_type(request,id):
    tasktype=TaskType.objects.get(id=id)
    tasktype.delete()
    return redirect ("/admi#n-dashboard/view-all-tasktype/")



def add_system_details(request):
    if request.method == 'POST':
        form = SystemDetailForm(request.POST)
        # print(form)
        system_type = request.POST["system_type"]
        specification = request.POST["specification"]
        system_service = request.POST["system_service"]
        system_id = request.POST["system_id"]
        added_on = request.POST["added_on"]
        if form.is_valid():
            f = form.save()
            f.system_type =system_type
            f.specification =specification
            f.system_service =system_service
            f.system_id =system_id
            f.added_on =added_on
            f.save()
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
        systemdetail.save()

        added=True
        return redirect("/admin-dashboard/view-all-system-details/")
    return render(request, "admindashboard/update_system_detail.html", locals())

def delete_system_details(request,pk):
      systemdetail=system_detail.objects.get(pk=pk)
      systemdetail.delete()
      return redirect("/admin-dashboard/view-all-system-details/")


def add_new_assigned_system_detail(request):
    user=User.objects.all()
    systemdetail=system_detail.objects.all()
    if request.method == "POST":
        form =SystemAssignedDetailForm(request.POST)
        # print(form)
        system_id = request.POST["system_id"]
        user = request.POST["user"]
        assigned_type = request.POST["assigned_type"]
        assigned_on = request.POST["assigned_on"]
        if form.is_valid():
            f1 = form.save()
            f1.assigned_type = assigned_type
            f1.assigned_on = assigned_on
            f1.save()
            # form.save()
            added = True
        else:
            if request.POST['system_id']=="":
                sysnotadd=True
            notadd=True

    else:
        form =SystemAssignedDetailForm(request.POST)
    return render(request, "admindashboard/add_new_assigned_system_detail.html", locals())

def view_all_assigned_system_detail(request):
    assignedsystem= Assigned_System_Detail.objects.all()
    return render(request, "admindashboard/view_all_assigned_system_detail.html", locals())

def update_assigned_system_details(request,id):
    user = User.objects.all()
    systemdetail = system_detail.objects.all()
    assignedsystem=Assigned_System_Detail.objects.get(id=id)

    if request.method == "POST":
        assignedsystem.system_id= request.POST["system_id"]
        assignedsystem.user= request.POST["user"]
        assignedsystem.assigned_type = request.POST["assigned_type"]
        assignedsystem.save()

        added=True
        return redirect("/admin-dashboard/view-all-assigned-system-details/")
    return render(request, "admindashboard/update_assigned_system_detail.html", locals())

def delete_assigned_system_details(request,id):
     assignedsystem=Assigned_System_Detail.objects.get(id=id)
     assignedsystem.delete()
     return redirect("/admin-dashboard/view-all-assigned-system-details/")



def view_all_user_task(request):
    usertask = Task.objects.all()
    return render(request, "admindashboard/view_all_user_task.html", locals())

def view_single_user_task(request,id):
        task=Task.objects.get(id=id)
        uploaded_files_data = task_uploaded_file.objects.filter(task__id=id)
        for i in  uploaded_files_data:
            print(i.uploaded_file)

        return render(request,"admindashboard/view_single_user_task.html", locals())



def view_all_user_project(request):
    userproject=Project.objects.all()
    return render(request,"admindashboard/view_all_user_project.html",locals())


def view_single_user_project(request,project_id):
    userproject=Project.objects.get(id=project_id)
    task_details = Task.objects.filter(project_id=project_id).order_by('-id')
    uploaded_files_data = task_uploaded_file.objects.filter(task__project_id=project_id)
    return render(request,"admindashboard/view_single_user_project.html",locals())



def view_user_contact(request):
    user_detail=User.objects.all()
    return render(request,"admindashboard/view_user_contact.html",locals())



def view_single_user_all_task(request,user_id):
   taskdetail=Task.objects.filter(user_id=user_id)
   userdetail=User.objects.filter(id=user_id)
   return  render(request,"admindashboard/single_user_all_task.html",locals())


def view_single_user_all_project(request,user_id=None):
    all_projects = Project.objects.filter(user_id=user_id).order_by('-id')
    userdetail = User.objects.filter(id=user_id)
    return render(request,"admindashboard/view_single_user_all_project.html",locals())


def view_all_user_attendance(request):
    view_user = User.objects.all()
    return render(request,"admindashboard/view_all_user_attendence.html",locals())

def view_single_user_attendence(request,user_id):
    get_detail=Detail_attendence.objects.filter(user_id=user_id)
    userdetail = User.objects.filter(id=user_id)
    return render(request,"admindashboard/view_single_user_attendence.html",locals())

def view_today_all_attendence(request):
    today=Attendence.objects.filter(attend_date=datetime.now().date())
    return render(request, "admindashboard/view_today_all_attendence.html", locals())


def add_holidays(request):
    if request.method == "POST":
        form = holidaysForm(request.POST)
        print(form)
        from_date = request.POST["from_date"]
        to_date = request.POST["to_date"]
        event_name = request.POST["event_name"]
        if form.is_valid():
            f1 = form.save()
            f1.from_date = from_date
            f1.to_date = to_date
            f1.event_name = event_name
            f1.save()
            added = True
    else:
        form = holidaysForm(request.POST)
    return render(request,"admindashboard/add_holidays.html",locals())