from django.urls import path

from task.views import *

app_name = 'task'

urlpatterns = [
    path('', index, name='home'),
    path('categories/', category, name='category'),
    path('category/<int:category_id>/', category_detail, name='category_detail'),
    path('subject/', subject, name='subject'),
    path('subject/<int:subject_id>/', subject_detail, name='subject_detail'),
    path('task/<int:task_id>/', task_detail, name='task_detail'),

]
