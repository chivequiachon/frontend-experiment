from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse

def home_page(request):
	return render(request, 'index.html')
    #return redirect(reverse('home_page'))