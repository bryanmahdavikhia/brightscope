from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def main(request):
    # return HttpResponse("Hello, world. You're at the home index.")
    return render(request, 'home.html')

def program(request):
    return render(request, 'program.html')

def fasilitas(request):
    return render(request, 'fasilitas.html')

