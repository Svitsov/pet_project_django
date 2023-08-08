from django.contrib import admin
from .models import *


class TaskImageAdmin(admin.ModelAdmin):
    pass


class TaskImageInline(admin.StackedInline):
    model = TaskImage
    max_num = 10
    extra = 0


class TaskAdmin(admin.ModelAdmin):
    inlines = [TaskImageInline, ]
    list_display = (
        'id', 'title', 'pub_date',
        'time_update', 'category',
        'author', 'subject', 'is_published'
    )
    list_display_links = ('id', 'title')
    search_fields = ('title', 'description')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'pub_date')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title')


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'text')
    list_display_links = ('id', 'text')
    search_fields = ('id', 'text')


admin.site.register(TaskImage, TaskImageAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Comment, CommentAdmin)
