import datetime
from django import template
from django.http import HttpResponse
from django.shortcuts import render_to_response, render

def index(request):
    return HttpResponse("Hello Django")

def today_is(request):
    now = datetime.datetime.now()
    return render(request, 'blog/datetime.html', {
        'now': now, 
        'template_name': 'blog/nav.html', }
        )