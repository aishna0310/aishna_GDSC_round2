from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save() #to save the
			username = form.cleaned_data.get('username')
			messages.success(request, f'Your account has been created! You are now able to login')
			return redirect('login')
	else:
		form = UserCreationForm()

	return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
	return render(request, 'users/profile.html')#first argument always request
