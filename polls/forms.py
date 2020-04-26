from django import forms
from .models import Departments, Classes, Sections
from django.utils.translation import ugettext_lazy as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Button
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
            'dept_name': _('Less than 40 characters'),
        }
        error_messages = {        
            'dept_name': {
                'max_length': _("This department's name is too long."),
            }
        }
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.form_method = 'post'
    #     self.helper.add_input(Submit('submit', 'Save', css_class = 'btn-primary'))
    #     self.helper.add_input(Button('cancel', 'Cancel', css_class='btn-danger',
    #                          href="{% url 'departments' %}"))

class ClassesForm(forms.ModelForm):
    class Meta:
        model = Classes
        fields = ('subject_number', 'title')
        labels = {
            'subject_number': _('Subject Number'),
            'title': _('Title'),
        }
        help_texts = {
            'subject_number': _('Less than 10 characters'),
            'title': _('Less than 100 characters'),
        }
        error_messages = {        
            'subject_number': {
                'max_length': _("The subject name is too long."),
            },
            'title': {
                'max_length': _("The title is too long."),
            },
        }
    departments = forms.ModelChoiceField(queryset=Departments.objects.all())
    def __init__(self, *args, **kwargs):
        # Only in case we build the form from an instance
        # (otherwise, 'toppings' list should be empty)
        if kwargs.get('instance'):
            # We get the 'initial' keyword argument or initialize it
            # as a dict if it didn't exist.
            initial = kwargs.setdefault('initial', {})
            # The widget for a ModelMultipleChoiceField expects
            # a list of primary key for the selected data.
            initial['departments'] = [t.pk for t in kwargs['instance'].departments_set.all()]
        forms.ModelForm.__init__(self, *args, **kwargs)

    def save(self, commit=True):
        # Get the unsaved Pizza instance
        instance = forms.ModelForm.save(self, False)
        # Prepare a 'save_m2m' method for the form,
        old_save_m2m = self.save_m2m
        def save_m2m():
            old_save_m2m()
            # This is where we actually link the pizza with toppings
            instance.departments_set.clear()
            for department in self.cleaned_data['departments']:
                instance.departments_set.add(department)
        self.save_m2m = save_m2m
        # Do we need to save all changes now?
        # Just like this
        # if commit:
        instance.save()
        self.save_m2m()
        return instance
    
class SectionsForm(forms.ModelForm):
    class Meta:
        model = Sections
        fields = ('crn', 'subject_number', 'name', 'credithours', 'sectiontype', 'starttime', 'endtime', 'dayofweek', 'gpa')
        labels = {
            'crn': _('CRN'),
            'subject_number': _('Subject Number'),
            'name': _('Name'),
            'credithours': _('Credit Hours'),
            'sectiontype': _('Section Type'),
            'starttime': _('Start Time'),
            'endtime': _('End Time'),
            'dayofweek': _('Day of Week'),
            'gpa': _('GPA'),
        }
