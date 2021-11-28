from django.contrib import admin
from .models import Question, Answer

# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question', 'category','status','added_date']
    
admin.site.register(Question, QuestionAdmin)

class AnswerAdmin(admin.ModelAdmin):
    list_display = ['question', 'answer', 'added_date', 'up_voting', 'down_voting']
admin.site.register(Answer, AnswerAdmin)