from django.shortcuts import render
from taskapp.models import *
# Create your views here.

def all_users(request,layout=None):
    all_users_admin_data=User.objects.filter(is_superuser=True)
    all_employees_data=User.objects.filter(is_superuser=False)
    if layout is None:
        return render(request,"admindashboard/all_users_table_layout.html",locals())

    if layout =="tabular":
        return render(request,"admindashboard/all_users_table_layout.html",locals())
    if layout =="grid":
        return render(request,"admindashboard/all_users_grid_layout.html",locals())
