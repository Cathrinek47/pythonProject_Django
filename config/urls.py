from django.contrib import admin
from django.urls import path, include
from task_manager.views import *


urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', include('new_app.urls')),
    # path('tasks/', TaskListCreateView.as_view(), name='get_tasks'),
    path('tasks/', task_list_create, name='get_tasks'),
    path('tasks/status/', get_tasks_filtered, name='filter_tasks'),
    path('tasks/statistic/', TaskStatisticView.as_view(), name='task-stats'),
    path('tasks/<int:pk>/', task_detail_update_delete, name='task_detail_update_delete'),
    # path('', include('library.urls')),
]
