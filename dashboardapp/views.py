from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from taskapp.models import *
# Create your views here.
def dashboard_index(request):
    # print(User.objects.all()[0])
    if not request.user.is_superuser:
        employee_tab=True
        user_tasks_count=Task.objects.filter(user=request.user).count()
        user_project_count=Project.objects.filter(user=request.user).count()

        # task_details=Task.objects.values_list('task_type__type_name',flat=True).filter(user=request.user)

        # page_list = list()
        #
        # for link in task_details:
        #
        #     page_list.append(link)
        # page_list=set(page_list)
    if request.user.is_superuser:
        super_user_tab=True
        total_users=User.objects.all().count()
        total_tasks=TaskType.objects.all().count()
        total_departments=ProgrammingLanguage.objects.all().count()
        total_systems=system_detail.objects.all().count()
        total_user_task=Task.objects.all().count()
        total_user_project=Project.objects.all().count()

    return render(request,"dashboardapp/dashboard_home.html",locals())

    

def profile(request):
    if request.method == 'POST' and request.FILES['upload']:
        upload = request.FILES['upload']
        user_db=User.objects.get(id=request.user.id)
        user_db.display_pic=upload
        user_db.profile_updated=True
        user_db.save()
        # fss = FileSystemStorage()
        # file = fss.save(upload.name, upload)
        # file_url = fss.url(file)
    return render(request,"dashboardapp/profile.html",locals())