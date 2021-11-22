from django.urls import path

from admindashboard import views

urlpatterns = [
    path('all-users/', views.all_users),
    path('all-users/<str:layout>/', views.all_users),

    # path('view-chart',views.view_chart),

]
