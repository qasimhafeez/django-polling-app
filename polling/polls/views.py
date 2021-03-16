from django.shortcuts import render
from .models import Question, Choice
from django.http import Http404

# Create your views here.

def index(req):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {"latest_question_list": latest_question_list}
    return render(req, "polls/index.html", context)

def detail(req, question_id):
    try:
        question = Question.objects.get(pk=question.id)
    except Question.DoesNotExist:
        raise Http404("Question does not exists")
    return render(req, 'polls/result.html', {"question": question})