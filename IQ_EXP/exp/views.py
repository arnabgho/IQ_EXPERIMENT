from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader
# Create your views here.

from .models import Sets

def index(request):
	#return HttpResponse("Hello World, You are at the Experiment Index")
	template=loader.get_template('exp/index.html')
	
	list_sets=Sets.objects.all()
	context={'set_list':list_sets,}
	return HttpResponse(template.render(context,request))

def set_1(request):
	template=loader.get_template('exp/set_1.html')
	context={}
	return HttpResponse(template.render(context,request))

