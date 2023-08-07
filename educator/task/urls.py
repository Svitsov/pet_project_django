from django.urls import path

from task.views import *

urlpatterns = [
    path('', index, name='home'),
    # path('categories/', category, name='category'),
    # path('category/<slug:slug>/', category_detail, name='category_detail'),
    # path('categories/', category, name='category'),
]
