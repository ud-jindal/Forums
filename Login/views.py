from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.
from .models import User
def Register(request):
	if request.POST:
		u = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
		u.first_name = request.POST['fname']
		u.last_name = request.POST['lname']
		return render(request, 'Login/Login.html', {'register' : 1})
	return render(request, 'Login/Register.html')

def Login(request):
	if(request.session.get('logged_in', False)):
			return render(request, 'Login/index.html')
	if request.POST:
		try:
			user = User.objects.get(username=request.POST['username'])
			if(user.check_password(request.POST['password'])):
				pass
			else:
				return render(request, 'Login/Login.html', {'status' : 1})
		except:
			return render(request, 'Login/Login.html', {'status' : 1})
		request.session['logged_in'] = True
		request.session['user'] = user.username
		return render(request, 'Login/index.html')	
	return render(request, 'Login/Login.html')

def Logout(request):
	request.session['logged_in'] = False
	request.session['user'] = None
	return HttpResponseRedirect('/login')