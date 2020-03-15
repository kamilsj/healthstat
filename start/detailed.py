from bokeh.io import output_notebook
from django.shortcuts import render, redirect

def index(request):
    data = {}
    return render(request, 'start/activities.html', {'data': data})
