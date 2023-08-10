import random

from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.utils.text import slugify

from .models import *

MENU = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить статью', 'url_name': 'add_page'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'},
        ]


def index(request):
    random_number = random.randint(1, 100000)
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
        'random_number': random_number,
    }
    return render(request, 'task/index.html', context=context)


def category(request):
    task = Task.objects.all()
    categories = Category.objects.all()
    subjects = Subject.objects.all()
    context = {
        'title': 'Главная страница',
        'menu': MENU,
        'task': task,
        'categories': categories,
        'subjects': subjects,
        'category_selected': 0,
    }
    return render(request, 'task/category.html', context)


def category_detail(request, category_id):
    categories = Category.objects.all()
    category = get_object_or_404(Category, id=category_id)
    category_subject = Subject.objects.filter(category=category)
    subjects = Subject.objects.all()

    context = {
        'title': 'Детали категории',
        'categories': categories,
        'menu': MENU,
        'category': category,
        'category_subject': category_subject,
        'subjects': subjects,
    }
    return render(request, 'task/category_detail.html', context=context)


def subject(request):
    task = Task.objects.all()
    categories = Category.objects.all()
    subjects = Subject.objects.all()
    context = {
        'title': 'Главная страница',
        'menu': MENU,
        'task': task,
        'categories': categories,
        'subjects': subjects,
        'category_selected': 0,
    }
    return render(request, 'task/subject.html', context=context)


def subject_detail(request, subject_id):
    categories = Category.objects.all()
    subjects = Subject.objects.all()
    subject = get_object_or_404(Subject, pk=subject_id)
    tasks = Task.objects.filter(subject=subject_id)
    context = {
        'title': subject.title,
        'menu': MENU,
        'subject': subject,
        'tasks': tasks,
        'categories': categories,
        'subjects': subjects,
    }
    return render(request, 'task/subject_detail.html', context)


def task_detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    categories = Category.objects.all()
    subjects = Subject.objects.all()
    images = TaskImage.objects.filter(task=task_id)
    comments = Comment.objects.filter(task=task_id)
    context = {
        'title': 'Главная страница',
        'menu': MENU,
        'task': task,
        'categories': categories,
        'subjects': subjects,
        'category_selected': 0,
        'images': images,
        'comments': comments,
    }
    return render(request, 'task/task_detail.html', context=context)


def search_results(request):
    query = request.GET.get('q')
    if query:
        tasks = Task.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )
        categories = Category.objects.filter(title__icontains=query)
        subjects = Subject.objects.filter(title__icontains=query)

        # Create separate lists for each model
        task_results = [{'model_name': 'task', 'object': task} for task in tasks]
        category_results = [{'model_name': 'category', 'object': category} for category in categories]
        subject_results = [{'model_name': 'subject', 'object': subject} for subject in subjects]

        # Combine the lists and sort by model name
        results = task_results + category_results + subject_results
        results.sort(key=lambda x: x['model_name'])

        # Преобразуем запрос в URL-совместимый формат
        slugified_query = slugify(query)
    else:
        results = []
        slugified_query = None

    context = {'results': results, 'slugified_query': slugified_query}
    return render(request, 'task/search_results.html', context)
