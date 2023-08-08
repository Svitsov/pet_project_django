from django.shortcuts import render, get_object_or_404

from .models import *

MENU = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить статью', 'url_name': 'add_page'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'},
        ]


def index(request):
    tasks = Task.objects.all()
    categories = Category.objects.all()
    subjects = Subject.objects.all()
    context = {
        'title': 'Главная страница',
        'menu': MENU,
        'tasks': tasks,
        'categories': categories,
        'subjects': subjects,
        'category_selected': 0,
    }
    return render(request, 'task/index.html', context=context)


def category(request):
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
    return render(request, 'task/category.html')


def category_detail(request, category_id):
    # categories = Category.objects.filter(pk=category_id)
    # task = Task.objects.all()
    # subjects = Subject.objects.all()
    # context = {
    #     'title': 'Главная страница',
    #     'menu': MENU,
    #     'task': task,
    #     'categories': categories,
    #     'subjects': subjects,
    #     'category_selected': 0,
    # }
    return render(request, 'task/category_detail.html')


def subject(request):
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
    return render(request, 'task/subject.html')


def subject_detail(request, subject_id):
    # subjects = Subjects.objects.filter(pk=subject_id)
    # task = Task.objects.all()
    # subjects = Subject.objects.all()
    # context = {
    #     'title': 'Главная страница',
    #     'menu': MENU,
    #     'task': task,
    #     'categories': categories,
    #     'subjects': subjects,
    #     'category_selected': 0,
    # }
    return render(request, 'task/subject_detail.html')


def task_detail(request, task_id):
    # task = Task.objects.filter(pk=task_id)
    # subjects = Subject.objects.all()
    # context = {
    #     'title': 'Главная страница',
    #     'menu': MENU,
    #     'task': task,
    #     'categories': categories,
    #     'subjects': subjects,
    #     'category_selected': 0,
    # }
    return render(request, 'task/task_detail.html')
