from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question, User
# from rest_framework.views import APIView


def rel(request):
    return render(request, 'polls/rel.html')

def insert(request):
    if request.method == 'POST':
        get_username = request.POST.get('username',None)
        get_password = request.POST.get('password',None)
    user = User()
    user.username = get_username
    user.password = get_password
    user.save()
    result = User.objects.all()
    return render(request, 'polls/relResults.html', {
        'username': result,
    })

def find(request):
    if request.method == 'POST':
        get_username = request.POST.get('username',None)
    result = User.objects.all()
    return render(request, 'polls/relResults.html', {
        'username': result,
    })

def delete(request):
    if request.method == 'POST':
        get_username = request.POST.get('username',None)
    User.objects.filter(username=get_username).delete()
    result = User.objects.all()
    return render(request, 'polls/relResults.html', {
        'username': result,
    })

def update(request):
    if request.method == 'POST':
        get_username = request.POST.get('username',None)
        get_password = request.POST.get('password',None)
    try:
        delete_user = User.objects.get(username=get_username) # object to update
    except User.DoesNotExist:
        # Redisplay the question voting form.
        result = User.objects.all()
        return render(request, 'polls/relResults.html', {
            'username': result,
            'error_message': "No such item.",
        })
    else:
        delete_user.password = get_password # update name
        delete_user.save() # save object    
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        result = User.objects.all()
        return render(request, 'polls/relResults.html', {
            'username': result,
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
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))