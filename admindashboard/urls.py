from django.urls import path

from admindashboard import views

urlpatterns = [
    path('all-users/', views.all_users),
    path('all-users/<str:layout>/', views.all_users),
    path('user-create/', views.add_new_user),
    path('create-language/', views.add_programming_language),
    path('view-all_users/', views.view_all_users),
    path('edit-user/<str:id>/', views.update_user),
    path('view-all_programming_language/', views.view_all_programming_language),
    path('edit-programming-language/<str:id>/',views.update_programming_language),

    # path('view-chart',views.view_chart),

]
