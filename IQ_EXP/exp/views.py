from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect

from django.template import loader
# Create your views here.

from .models import Sets
from utils.calculate_score import calc_score

def index(request):
	#return HttpResponse("Hello World, You are at the Experiment Index")
	template=loader.get_template('exp/index.html')
	
	list_sets=Sets.objects.all()
	context={'set_list':list_sets,}
	return HttpResponse(template.render(context,request))

def scores(request,score):
	template=loader.get_template('exp/scores.html')
	context={'score':score}
	return HttpResponse(template.render(context,request))

def set(request,id):
	template=loader.get_template('exp/set/'+str(id)+'.html')
	context={}
	return HttpResponse(template.render(context,request))

def result(request,set_id):
	# print request.POST['1']
	try:
		set_id_int=int(set_id)
	except ValueError:
		raise Http404()
	else:
		res_dict = dict(request.POST.iterlists())
		score=calc_score(res_dict,set_id)
		if(score!=-1):
			return HttpResponseRedirect('scores/'+str(score)+'/')
		else:		
			return render(request,'exp/set/'+str(set_id)+'.html',{'error':'true'})
