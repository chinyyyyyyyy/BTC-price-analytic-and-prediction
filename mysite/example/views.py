from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

d = dict()
d["day"] = 5


def index(request):
	return HttpResponse('<b>hello</b>')

def index2(request):
	return HttpResponse('<b>hellooooooooooooooooooo</b>')

def tutorial(request):
        return render(request, 'example/copy.html', d)
