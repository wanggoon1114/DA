from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def dummy(request):
    return render(render, 'index.html')
