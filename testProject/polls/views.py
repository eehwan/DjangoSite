from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(req):
    return HttpResponse("Hello World. You are at the polls index.")

def detail(request, question_id):
    return HttpResponse(f"You're looking at question {question_id}. <a href='./results'>Results</a> <a href='./vote'>Vote</a>")

def results(request, question_id):
    return HttpResponse(f"You're looking at the results of question {question_id}.")

def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}.")