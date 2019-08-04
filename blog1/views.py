from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
studInfo = [
    {
        'rno': '1',
        'name': 'Jeet',
        'address': 'Rajkot',
        'status': 'mojilo',
        'num':123456789
    },
    {
        'rno': '2',
        'name': 'Neeraj',
        'address': 'Rajkot',
        'status': 'mojilo2',
        'num':123456789
    },
    {
        'rno': '2',
        'name': 'Neeraj',
        'address': 'Rajkot',
        'status': 'mojilo2',
        'num':123456789
    }
    
]


def index(request):
    # return HttpResponse("HelloWorld")
    context = {
        'studData': studInfo
    }
    #data1 = {'data1':"This Data is coming from Views.PY"}
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html', {'title': 'About Us'})
