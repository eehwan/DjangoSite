from django.shortcuts import render
from django.http import HttpResponse
from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = "<div>Hello World. You are at the polls index.<div>"
    for question in latest_question_list:
        output += f"<a href='./{question.id}'>{question.question_text}</a>"
    return HttpResponse(output)

def detail(request, question_id):
    return HttpResponse(f"You're looking at question {question_id}. <a href='./results'>Results</a> <a href='./vote'>Vote</a>")

def results(request, question_id):
    return HttpResponse(f"You're looking at the results of question {question_id}.")

def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}.")