"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from core import settings
from indexapp import views
urlpatterns = [
    # path('admin/view-user-performance/<str:id>', views.view_chart),
    path('admin/', admin.site.urls),
    path('', views.index_view),
    path('reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',
         views.reset, name='reset'),
    path('password-forgot/', views.password_reset),

    # path('logout',views.logout_view),
    # path('tasks',views.all_tasks),
    # path('add-task',views.add_task),
    # path('view-task/<str:id>',views.view_task),
    # path('edit-task/<str:id>',views.edit_task),
    path('dashboard/', include('dashboardapp.urls')),
    path('tasks/', include('taskapp.urls')),
    path('projects/', include('projectapp.urls')),
    path('admin-dashboard/', include('admindashboard.urls')),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    # path('view-chart',views.view_chart),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
   import debug_toolbar
   urlpatterns += [
       url(r'^__debug__/', include(debug_toolbar.urls)),
   ]
