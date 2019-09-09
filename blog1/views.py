from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,Http404
from blog1.models import studInfo,studResult
from blog1.forms import abtusfrm,dataForm
from datetime import date
import time
# Create your views here.
# studInfo = [
#     {
#         'rno': '1',
#         'name': 'Jeet',
#         'address': 'Rajkot',
#         'status': 'mojilo',
#         'dob':date.today(),
#         'car':None,
#         'data':12645423        
        
#     },
#     {
#         'rno': '2',
#         'name': 'Neeraj',
#         'address': 'Rajkot',
#         'status': 'mojilo2',
#         'dob':'Fri 2 Jul 2019',
#         'movie':'Batman & Robin',
#         'car':None
        
#     },
#       {
#         'rno': '3',
#         'name': 'Deep',
#         'address': 'Japan    Jamkhabhadiya',
#         'status': 'mojilo',
#         'dob':'Fri 26 Jul 2019',
#         'car':None,
#         'urldata': 'http://google.com?=falanudhiknu'
#     },
#     {
#         'rno': '4',
#         'name': 'Yashraj',
#         'address': 'Japan',
#         'status': 'mojilo2',
#         'dob':'Fri 26 Jul 2019',
#         'car':None,
#         'filestype':"""one
#         two
#         three"""
#     }
# ]


def index(request):    

    studInfo_data = studInfo.objects.order_by('rno')    
    studResult_data = studResult.objects.order_by('sInfo')

    context = {
        'studData': studInfo_data,
        'studResultdata':studResult_data
    }    
    return render(request, 'index.html', context)

# Decorator
# @login_required(login_url='/admin/login/') 

def about(request,rno):    
    # res =  HttpResponse()
    # if request.user.is_authenticated:
    #     res.content = "<html><b>Your Welcome</b></html>"
    # else:
    #     raise Http404
    #     # return HttpResponseRedirect('/admin/login/?next=/about/')
    # res.write("Page Not Found.")
    # print(request.user)
    # print(dir(request))
    # print(res.status_code)
    # res.status_code = 404
    # print(res.status_code)
    # return res

    instance = studInfo.objects.get(rno=rno)
    about_us_frm = dataForm(request.POST or None,instance=instance)
    
    if about_us_frm.is_valid():
        # print("data executed",request.POST)
        about_us_frm.save()
        
    context = {
        'title': 'About Us',
        'about_us_frm':about_us_frm,
        }
        
    return render(request, 'about.html',context )
