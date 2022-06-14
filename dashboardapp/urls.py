from django.urls import path

from dashboardapp import views

urlpatterns = [
    path('', views.dashboard_index),
    path('profile', views.profile),
    # path('view-chart',views.view_chart),
]
