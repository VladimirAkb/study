from django.shortcuts import render
import random

def home(request):
    return render(request, 'main/home.html')

def data(request):
    generated_data = [random.randint(1, 100) for _ in range(5)]
    return render(request, 'main/data.html', {'data': generated_data})

def test(request):
    return render(request, 'main/test.html')
