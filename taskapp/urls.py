from django.urls import path

from taskapp import views

urlpatterns =[
    path('', views.all_tasks),
    path('add-task', views.add_task),
    path('view-task/<str:id>', views.view_single_task),
    path('edit-task/<str:id>', views.edit_task),
    path('task-type/<str:type>', views.task_type),
    path('view-user-reporting-to/',views.contact_user_reporting_to),
    path('delete-task/<str:id>', views.delete_task),
    path('view-user-team-member/', views.contact_team_members),
    # path('view-chart',views.view_chart),

]
