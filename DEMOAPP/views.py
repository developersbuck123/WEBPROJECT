from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def hi(request):
    return render(request, 'DEMOAPP/hi.html')


def home(request):
    data = request.POST.get('txtname')
    print(data)
    return render(request, 'DEMOAPP/home.html', {'data': data})
