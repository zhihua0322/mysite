from django import forms
from .models import Choice, Question, User, Departments, Courses
from django.utils.translation import ugettext_lazy as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.urls import reverse_lazy

class DepartmentsForm(forms.ModelForm):
    class Meta:
        model = Departments
        fields = ('dept_id', 'dept_name')
        labels = {
            'dept_id': _('Department ID'),
            'dept_name': _('Department Name'),
        }
        help_texts = {
            'dept_id': _('Integer'),
            'dept_name': _('Less than 50 characters'),
        }
        error_messages = {        
            'dept_name': {
                'max_length': _("This department's name is too long."),
            }
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save Departments', css_class = 'btn-primary'))