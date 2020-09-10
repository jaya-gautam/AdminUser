from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, authenticate
from UserApp.forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.contrib.auth import get_user_model




def loginview(request):
	if request.method == 'POST':
		form = AuthenticationForm(request=request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				form = AuthenticationForm()
				return render(request, 'Registration/login.html', {'form':form, 'msg':'Invalid Credentials'})
		else:
			return redirect('signup')
	form = AuthenticationForm()
	return render(request, 'Registration/login.html', {'form':form})


def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			plogin(request, user)
			#return HttpResponse('success')
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'Registration/signup.html', {'form': form})





def home(request):
	all_users= get_user_model().objects.all()
	return render(request, 'Registration/home.html', {'all_users':all_users})


def delete(request, usr):
	user = get_user_model().objects.filter(username  = usr)
	user.delete()
	all_users= get_user_model().objects.all()
	return render(request, 'Registration/home.html', {'all_users':all_users , 'msg': 'user is successfully deleted'})
