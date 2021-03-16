from django.shortcuts import render
from .models import Question, Choice

# Create your views here.

def index(req):
    return render(req, "polls/index.html")