from django.shortcuts import render
from django.http import HttpResponse

def index(req):
    return HttpResponse("<a href='/admin'>admin</a> <a href='/polls'>polls</a>")