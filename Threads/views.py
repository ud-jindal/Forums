from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from Login.models import User
from .models import Thread, Comment
# Create your views here.
def Home(request):
	if(not request.session['logged_in']):
		return HttpResponseRedirect('/login/')
	return HttpResponseRedirect('/threads/'+str(request.session['user'])+'/')

def Threads(request, username):
	try:
		user = User.objects.get(username=username)
		threadlist = Thread.objects.all()
		if(request.session['logged_in']):
			return render(request, 'Threads/threads.html', {'threadlist' : threadlist})
		else:
			return HttpResponseRedirect('/login/')
	except:
		return HttpResponseRedirect('/login/')

def createThread(request, username):
	if request.POST:
		thread = Thread()
		thread.text = request.POST['thread']
		thread.author = User.objects.get(username=username)
		thread.save()
		return HttpResponseRedirect('/threads/')
	user = User.objects.get(username=username)
	return render(request, 'Thread/create.html', {'User' : user})