from django.shortcuts import render
from django.http import HttpResponse
from account.decorators import authenticated_user

@authenticated_user
def home(request):
	return render(request, "main/home.html")