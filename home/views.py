from django.shortcuts import *
from django.http import *
from django.template.response import TemplateResponse
# Create your views here.

def index(request):
	return render(request,'index.html',{})


def sendmail(request):
	name = request.POST['name']
	email = request.POST['email']
	subject = request.POST['subject']
	message = request.POST['message']
	return redirect('index')