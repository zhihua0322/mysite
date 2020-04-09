import datetime

from django.db import models
from django.utils import timezone
# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200, default="0000")
    def __str__(self):
        return self.username

class Departments(models.Model):
    dept_id = models.IntegerField(db_column='Dept_ID', blank=True, primary_key=True)  # Field name made lowercase.
    dept_name = models.CharField(db_column='Dept_Name', max_length=40, blank=True, null=True)  # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'departments'

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text