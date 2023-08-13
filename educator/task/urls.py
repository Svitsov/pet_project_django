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
    path('search/', search_results, name='search'),
    path('toggle_like/<int:task_id>/', toggle_like, name='toggle_like'),
    path('toggle_dislike/<int:task_id>/', toggle_dislike, name='toggle_dislike'),
    path('load_more_comments/<int:task_id>/', load_more_comments, name='load_more_comments'),
    path('profile/<str:username>/', profile, name='profile'),

]
