import datetime

from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200, default="0000")
    def __str__(self):
        return self.username

class Departments(models.Model):
    dept_id = models.IntegerField(db_column='Dept_ID', blank=True, primary_key=True)  # Field name made lowercase.
    dept_name = models.CharField(db_column='Dept_Name', max_length=40, blank=True, null=True)  # Field name made lowercase.
    def get_absolute_url(self):
        return reverse('polls:departments_detail', kwargs={'pk': self.pk})
        # return '/departments'
    class Meta:
        managed = True
        db_table = 'departments'

class Courses(models.Model):
    crn = models.CharField(db_column='CRN', max_length=5, blank=True, primary_key=True)  # Field name made lowercase.
    subject = models.CharField(db_column='Subject', max_length=6, blank=True, null=True)  # Field name made lowercase.
    number = models.CharField(db_column='Number', max_length=5, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    credithours = models.CharField(db_column='CreditHours', max_length=30, blank=True, null=True)  # Field name made lowercase.
    section = models.CharField(db_column='Section', max_length=5, blank=True, null=True)  # Field name made lowercase.
    starttime = models.CharField(db_column='StartTime', max_length=15, blank=True, null=True)  # Field name made lowercase.
    endtime = models.CharField(db_column='EndTime', max_length=15, blank=True, null=True)  # Field name made lowercase.
    dayofweek = models.CharField(db_column='DayOfWeek', max_length=10, blank=True, null=True)  # Field name made lowercase.
    room = models.CharField(db_column='Room', max_length=10, blank=True, null=True)  # Field name made lowercase.
    building = models.CharField(db_column='Building', max_length=100, blank=True, null=True)  # Field name made lowercase.
    instructors = models.CharField(db_column='Instructors', max_length=450, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'courses'


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