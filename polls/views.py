from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.db.models import Count
from .models import Departments, Classes, Sections
from .forms import DepartmentsForm, ClassesForm, SectionsForm

# from rest_framework.views import APIView


# def rel(request):
#     return render(request, 'polls/rel.html')

# def insert(request):
#     if request.method == 'POST':
#         get_deptID = request.POST.get('Dept_ID',None)
#         get_deptname = request.POST.get('Dept_Name',None)
#     department = Departments()
#     department.dept_id = get_deptID
#     department.dept_name = get_deptname
#     department.save()
#     result = Departments.objects.all()
#     return render(request, 'polls/relResults.html', {
#         'departments': result,
#     })

# def find(request):
#     if request.method == 'POST':
#         get_deptID = request.POST.get('Dept_ID',None)
#     try:
#         result = Departments.objects.filter(dept_id=get_deptID) # object to update
#     except Departments.DoesNotExist:
#         return render(request, 'polls/relResults.html', {
#             'departments': result,
#             'error_message': "No such item.",
#         })
#     else:
#         return render(request, 'polls/relResults.html', {
#             'departments': result,
#         })

# def delete(request):
#     if request.method == 'POST':
#         get_deptID = request.POST.get('Dept_ID',None)
#     Departments.objects.get(dept_id=get_deptID).delete()
#     result = Departments.objects.all()
#     return render(request, 'polls/relResults.html', {
#         'departments': result,
#     })

# def update(request):
#     if request.method == 'POST':
#         get_deptID = request.POST.get('Dept_ID',None)
#         get_deptname = request.POST.get('Dept_Name',None)
#     try:
#         delete_department = Departments.objects.get(dept_id=get_deptID) # object to update
#     except Departments.DoesNotExist:
#         # Redisplay the question voting form.
#         result = Departments.objects.all()
#         return render(request, 'polls/relResults.html', {
#             'departments': result,
#             'error_message': "No such item.",
#         })
#     else:
#         delete_department.dept_name = get_deptname # update name
#         delete_department.save() # save object    
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # department hits the Back button.
#         result = Departments.objects.all()
#         return render(request, 'polls/relResults.html', {
#             'departments': result,
#         })

# def building(request):
#     if request.method == 'POST':
#         get_building = request.POST.get('Building', None)
#     numberofCourses = Courses.objects.values('building').annotate(num=Count('crn')).filter(building=get_building)
#     print(numberofCourses)
#     return render(request, 'polls/relResults.html', {
#         'building': get_building,
#         'numberofCourses': numberofCourses,
#     })


def homepage(request):
    return render(request, 'homepage.html')

def dashboard(request):
    return render(request, 'polls/dashboard.html')

class DepartmentsListView(generic.ListView):
    model = Departments
    context_object_name = 'departments_list'
    template_name = 'polls/departments_list.html'

class DepartmentsCreateView(generic.CreateView):
    model = Departments
    form_class = DepartmentsForm
    template_name = 'polls/departments_create.html'
    slug_url_kwarg = 'department_slug'

class DepartmentsUpdateView(generic.UpdateView):
    model = Departments
    form_class = DepartmentsForm
    template_name = 'polls/departments_update.html'
    slug_url_kwarg = 'department_slug'
    pk_url_kwarg = 'department_slug'
    def get_success_url(self):
        return reverse('polls:departments_detail', kwargs={'department_slug': self.object.dept_id})

    # def get(self, request, **kwargs):
    #     self.object = User.objects.get(username=self.request.user)
    #     form_class = self.get_form_class()
    #     form = self.get_form(form_class)
    #     context = self.get_context_data(object=self.object, form=form)
    #     return self.render_to_response(context)
    # def form_valid(self, form):
    #     self.object = form.save(commit=False)
    #     self.object.user = self.request.user
    #     self.object.save()
    #     return HttpResponseRedirect(self.get_success_url())
    # def get_object(self, queryset=None):
    #     return self.request.user

class DepartmentsDetailView(generic.DetailView):
    model = Departments
    slug_url_kwarg = 'department_slug'
    pk_url_kwarg = 'department_slug'
    template_name = 'polls/departments_detail.html'


class DepartmentsDeleteView(generic.DeleteView):
    model = Departments
    pk_url_kwarg = 'department_slug'
    template_name = 'polls/departments_delete.html'
    success_url = reverse_lazy('polls:departments')


class ClassesListView(generic.ListView):
    model = Classes
    context_object_name = 'classes_list'
    template_name = 'polls/classes_list.html'

class ClassesCreateView(generic.CreateView):
    model = Classes
    form_class = ClassesForm
    template_name = 'polls/classes_create.html'
    slug_url_kwarg = 'class_slug'

class ClassesDetailView(generic.DetailView):
    model = Classes
    template_name = 'polls/classes_detail.html'
    context_object_name = 'class'
    slug_url_kwarg = 'class_slug'
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['sections_list'] = Sections.objects.filter(subject_number=self.object.class_slug)
        context['departments_list'] = Departments.objects.filter(classes_contains__subject_number__startswith=self.object.class_slug)
        return context

class ClassesDeleteView(generic.DeleteView):
    model = Classes
    context_object_name = 'class'
    template_name = 'polls/classes_delete.html'
    success_url = reverse_lazy('polls:classes')

class ClassesUpdateView(generic.UpdateView):
    model = Classes
    form_class = ClassesForm
    template_name = 'polls/classes_update.html'
    slug_url_kwarg = 'class_slug'
    def get_success_url(self):
        return reverse('polls:classes_detail', kwargs={'class_slug': self.object.class_slug})

class SectionsListView(generic.ListView):
    model = Sections
    context_object_name = 'sections_list'
    template_name = 'polls/sections_list.html'

class SectionsCreateView(generic.CreateView):
    model = Sections
    form_class = SectionsForm
    template_name = 'polls/sections_create.html'
    slug_url_kwarg = 'crn'

# class IndexView(generic.ListView):
#     template_name = 'polls/index.html'
#     context_object_name = 'latest_question_list'

#     def get_queryset(self):
#         """Return the last five published questions."""
#         return Question.objects.order_by('-pub_date')[:5]


# class DetailView(generic.DetailView):
#     model = Question
#     template_name = 'polls/detail.html'


# class ResultsView(generic.DetailView):
#     model = Question
#     template_name = 'polls/results.html'

# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'polls/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # department hits the Back button.
#         return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))