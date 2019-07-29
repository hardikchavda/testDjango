from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
import time
# Create your views here.
studInfo = [
    {
        'rno': '1',
        'name': 'Jeet',
        'address': 'Rajkot',
        'status': 'mojilo',
        'dob':date.today(),
        'car':None,
        'data':12645423        
        
    },
    {
        'rno': '2',
        'name': 'Neeraj',
        'address': 'Rajkot',
        'status': 'mojilo2',
        'dob':'Fri 2 Jul 2019',
        'movie':'Batman & Robin',
        'car':None
        
    },
      {
        'rno': '3',
        'name': 'Deep',
        'address': 'Japan    Jamkhabhadiya',
        'status': 'mojilo',
        'dob':'Fri 26 Jul 2019',
        'car':None,
        'urldata': 'http://google.com?=falanudhiknu'
    },
    {
        'rno': '4',
        'name': 'Yashraj',
        'address': 'Japan',
        'status': 'mojilo2',
        'dob':'Fri 26 Jul 2019',
        'car':None,
        'filestype':"""one
        two
        three"""
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
