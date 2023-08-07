from django.shortcuts import render, get_object_or_404

from .models import *

MENU = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить статью', 'url_name': 'add_page'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'},
        ]


def index(request):
    # task = Task.objects.all()
    # categories = Category.objects.all()
    # subjects = Subject.objects.all()
    # context = {
    #     'title': 'Главная страница',
    #     'menu': MENU,
    #     'task': task,
    #     'categories': categories,
    #     'subjects': subjects,
    #     'category_selected': 0,
    # }
    return render(request, 'task/index.html')
