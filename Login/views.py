from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.
from .models import User
def Register(request):
	if request.POST:
		return HttpResponse("You are Registered Successfully.")
	return render(request, 'Register.html')

def Login(request):
	if request.POST:
		try:
			user = User.objects.get(username=request.POST['username'])
		except:
			return render(request, 'Login/Login.html', {'status' : 1})

		return HttpResponse("You are Login Successfully.")
	return render(request, 'Login/Login.html')