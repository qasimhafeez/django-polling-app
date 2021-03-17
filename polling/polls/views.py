from django.shortcuts import get_object_or_404, render
from .models import Question, Choice
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def index(req):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {"latest_question_list": latest_question_list}
    return render(req, "polls/index.html", context)

def detail(req, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exists")
    return render(req, 'polls/detail.html', {"question": question})

def results(req, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(req, "polls/results.html", {"question": question})

def vote(req, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=req.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(req, "polls/detail.html", {"question": question, "error_message": "Please select a choice", })
    else:
        selected_choice.vote += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))