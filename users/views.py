from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


def register(request):
	"""Регестрация"""
	if request.method != 'POST':
		# Показать пустую форму регестрации
		form = UserCreationForm()
	else:
		# Обработка формы
		form = UserCreationForm(data=request.POST)

		if form.is_valid():
			new_user =form.save()
			# Авторизировать пользователя и редиректнуть его
			login(request, new_user)
			return redirect('page:accont')

	# Показать пустую или недействительную форму
	context = {'form': form}
	return render(request, 'registration/register.html', context)