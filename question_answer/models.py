from django.db import models
from category.models import Category
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    question = models.CharField(max_length=255)
    status= models.BooleanField(default=True)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.question)


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    answer = models.TextField()
    added_date = models.DateTimeField(auto_now_add=True)
    up_voting = models.IntegerField(default=0)
    down_voting = models.IntegerField(default=0)

    def __str__(self):
        return str(self.answer)