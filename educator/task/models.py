from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


class Task(models.Model):
    title = models.CharField(max_length=55, verbose_name='Задача')
    description = models.TextField(blank=True, verbose_name="Описание")
    code = models.TextField(blank=True, verbose_name="Python код")
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор'
    )
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")
    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Категория",
        related_name='category'
    )
    subject = models.ForeignKey(
        'Subject',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Тема",
        related_name='subject'
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('task_detail', kwargs={'task_id': self.pk})

    class Meta:
        verbose_name = 'Задачи'
        verbose_name_plural = 'Задачи'
        ordering = ['-pub_date', 'title']


class Category(models.Model):
    title = models.CharField(max_length=55, verbose_name='Категория')
    description = models.TextField(blank=True, verbose_name="Описание")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'category_id': self.pk})

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'
        ordering = ['title']


class Subject(models.Model):
    title = models.CharField(max_length=55, verbose_name='Тема')
    description = models.TextField(blank=True, verbose_name="Описание")
    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Категория",
        related_name='subject'
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('subject_detail', kwargs={'subject_id': self.pk})

    class Meta:
        verbose_name = 'Темы'
        verbose_name_plural = 'Темы'
        ordering = ['title']


class TaskImage(models.Model):
    image = models.ImageField(
        upload_to="photos/%Y/%m/%d/",
        verbose_name="Изображение",
        null=True,
    )
    task = models.ForeignKey(
        'Task',
        on_delete=models.CASCADE,
        null=True,
        verbose_name="Изображение",
        related_name='image',
    )

    class Meta:
        verbose_name = 'Изображения'
        verbose_name_plural = 'Изображения'
        ordering = ['task']


class Comment(models.Model):
    task = models.ForeignKey(
        'Task',
        on_delete=models.CASCADE,
        null=True,
        verbose_name="Комментарий",
        related_name='comment',
    )
    text = models.TextField(blank=True, verbose_name="Комментарий")

    class Meta:
        verbose_name = 'Комментарии'
        verbose_name_plural = 'Комментарии'
        ordering = ['task']
