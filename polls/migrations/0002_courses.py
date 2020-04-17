# Generated by Django 3.0.5 on 2020-04-09 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('crn', models.CharField(blank=True, db_column='CRN', max_length=5, primary_key=True, serialize=False)),
                ('subject', models.CharField(blank=True, db_column='Subject', max_length=6, null=True)),
                ('number', models.CharField(blank=True, db_column='Number', max_length=5, null=True)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=100, null=True)),
                ('credithours', models.CharField(blank=True, db_column='CreditHours', max_length=30, null=True)),
                ('section', models.CharField(blank=True, db_column='Section', max_length=5, null=True)),
                ('starttime', models.CharField(blank=True, db_column='StartTime', max_length=15, null=True)),
                ('endtime', models.CharField(blank=True, db_column='EndTime', max_length=15, null=True)),
                ('dayofweek', models.CharField(blank=True, db_column='DayOfWeek', max_length=10, null=True)),
                ('room', models.CharField(blank=True, db_column='Room', max_length=10, null=True)),
                ('building', models.CharField(blank=True, db_column='Building', max_length=100, null=True)),
                ('instructors', models.CharField(blank=True, db_column='Instructors', max_length=450, null=True)),
            ],
            options={
                'db_table': 'courses',
                'managed': True,
            },
        ),
    ]