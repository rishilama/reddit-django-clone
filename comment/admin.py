from django.contrib import admin
from django.db import models
from .models import Comment

# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    list_display = ['answer','comments', 'added_date']
admin.site.register(Comment, CommentAdmin)