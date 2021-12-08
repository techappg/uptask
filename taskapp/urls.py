from django.urls import path

from taskapp import views

urlpatterns =[
    path('', views.all_tasks),
    path('add-task', views.add_task),
    path('view-task/<str:task_id>', views.view_single_task),
    path('edit-task/<str:id>', views.edit_task),
    path('task-type/<str:type>', views.task_type),
    path('view-user-reporting-to/',views.contact_user_reporting_to)
    # path('view-chart',views.view_chart),

]
