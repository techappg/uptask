from django.urls import path

from admindashboard import views

urlpatterns = [

    # USER
    path('all-users/', views.all_users),
    path('all-users/<str:layout>/', views.all_users),
    path('user-create/', views.add_new_user),
    path('view-all_users/', views.view_all_users),
    path('edit-user/<str:id>/', views.update_user),
    path('delete-user/<str:id>/', views.delete_user),
    path('view-single-user/<str:id>/', views.view_single_user),

    # PROGRAMMING LANGUAGE
    path('create-language/', views.add_programming_language),
    path('view-all_programming_language/', views.view_all_programming_language),
    path('edit-programming-language/<str:id>/',views.update_programming_language),
    path('delete-programming-language/<str:id>/', views.delete_programming_language),

    # TASK
    path('create-tasktype/',views.add_new_task_type),
    path('view-all-tasktype/',views.view_all_tasktype),
    path('edit-task-type/<str:id>/',views.update_task_type),
    path('delete-task-type/<str:id>/',views.delete_task_type),

    # SYSTEM DETAIL
    path('create-system-details/',views.add_system_details),
    path('view-all-system-details/', views.view_all_system_details),
    path('edit-system-details/<str:pk>/',views.update_system_details),
    path('delete-system-details/<str:pk>', views.delete_system_details),
    path('view-single-system-details/<str:pk>/', views.view_single_system_details),









    # path('view-chart',views.view_chart),

]
