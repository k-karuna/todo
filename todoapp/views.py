from django.http import Http404
from django.shortcuts import render_to_response
from todoapp.models import Todo
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from todoapp.models import Todo
from django.utils import timezone
from datetime import datetime

def todolist(request):
	todos = Todo.objects.all().order_by('-id')
	return render_to_response('index.html', {'todos': todos})

@csrf_exempt
def add(request):
	if request.method == 'GET':
		raise Http404
	else:
		response_data = {}
		response_data['status'] = 'Added'
		deadline = datetime(int(request.POST.get('year')), int(request.POST.get('month')), int(request.POST.get('day')), int(request.POST.get('hrs')), int(request.POST.get('mins')), int(request.POST.get('sec')))
		todo = Todo(author=request.POST.get('author'), title=request.POST.get('title'), text=request.POST.get('text'), time=timezone.localtime(timezone.now()), deadline=deadline)
		todo.save()
		todos = Todo.objects.all().order_by('-id')[:1]
		return render_to_response('content.html', {'todos': todos})

@csrf_exempt
def delete(request):
	if request.method == 'GET':
		raise Http404
	else:
		id = request.POST.get('id')
		Todo.objects.get(id=int(id)).delete()
		response_data = {}
		response_data['id'] = id
		return HttpResponse(json.dumps(response_data), content_type="application/json")

@csrf_exempt
def check(request):
	if request.method == 'GET':
		raise Http404
	else:		
		response_data = {}
		id = request.POST.get('id')
		todo = Todo.objects.get(id=int(id))
		todo.isdone = not todo.isdone
		todo.save();
		response_data['isdone'] = todo.isdone
		return HttpResponse(json.dumps(response_data), content_type="application/json")
