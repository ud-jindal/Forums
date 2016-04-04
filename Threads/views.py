from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from Login.models import User
from .models import Thread, Comment
# Create your views here.
def Home(request):
	if(request.session['logged_in']):
		return HttpResponseRedirect('/threads/'+request.session['user']+'/')
	return HttpResponseRedirect('/login/')

def Threads(request, username):
	#try:
		user = User.objects.get(username=username)
		threadlist = Thread.objects.all()
		if(request.session['logged_in']):
			return render(request, 'Threads/threads.html', {'threadlist' : threadlist, 'User': user,})
		else:
			return HttpResponseRedirect('/login/')
	#except:
	#	return HttpResponseRedirect('/login/')

def createThread(request, username):
	if request.POST:
		thread = Thread()
		thread.text = request.POST['thread']
		thread.author = User.objects.get(username=username)
		thread.save()
		return HttpResponseRedirect('/threads/')
	user = User.objects.get(username=username)
	return render(request, 'Threads/create.html', {'User' : user})

def comment(request,  id):
	thread = Thread.objects.get(id=id)
	if request.POST:
		user = User.objects.get(username=request.session['user'])
		com = Comment()
		com.text = request.POST['comment']
		com.author = user
		com.thread = thread
		com.save()
		return HttpResponseRedirect('.')
	comments = thread.comment_set.all()
	return render(request, 'Threads/comments.html', {'thread': thread, 'Comments' : comments})