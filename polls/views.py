from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question, User, Departments
# from rest_framework.views import APIView


def rel(request):
    return render(request, 'polls/rel.html')

def insert(request):
    if request.method == 'POST':
        get_deptID = request.POST.get('Dept_ID',None)
        get_deptname = request.POST.get('Dept_Name',None)
    department = Departments()
    department.dept_id = get_deptID
    department.dept_name = get_deptname
    department.save()
    result = Departments.objects.all()
    return render(request, 'polls/relResults.html', {
        'departments': result,
    })

def find(request):
    if request.method == 'POST':
        get_deptID = request.POST.get('Dept_ID',None)
    result = Departments.objects.all()
    return render(request, 'polls/relResults.html', {
        'departments': result,
    })

def delete(request):
    if request.method == 'POST':
        get_deptID = request.POST.get('Dept_ID',None)
    Departments.objects.filter(dept_id=get_deptID).delete()
    result = Departments.objects.all()
    return render(request, 'polls/relResults.html', {
        'departments': result,
    })

def update(request):
    if request.method == 'POST':
        get_deptID = request.POST.get('Dept_ID',None)
        get_deptname = request.POST.get('Dept_Name',None)
    try:
        delete_department = Departments.objects.get(dept_id=get_deptID) # object to update
    except Departments.DoesNotExist:
        # Redisplay the question voting form.
        result = Departments.objects.all()
        return render(request, 'polls/relResults.html', {
            'departments': result,
            'error_message': "No such item.",
        })
    else:
        delete_department.dept_name = get_deptname # update name
        delete_department.save() # save object    
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # department hits the Back button.
        result = Departments.objects.all()
        return render(request, 'polls/relResults.html', {
            'departments': result,
        })


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # department hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))