# Generated by Django 3.0.5 on 2020-04-26 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20200426_0243'),
    ]

    operations = [
        migrations.AddField(
            model_name='classes',
            name='class_slug',
            field=models.SlugField(default='', editable=False),
        ),
    ]
